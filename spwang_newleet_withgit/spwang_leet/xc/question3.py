import concurrent.futures
import psutil
import requests
import argparse
import time
import threading
import logging
from typing import Optional
from requests.exceptions import RequestException


class StressTester:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=config.concurrency
        )
        self.stop_event = threading.Event()
        self.stats_lock = threading.Lock()
        self.success_count = 0
        self.failure_count = 0
        self.memory_limit = config.memory_limit * 1024 * 1024  # 转换为字节

        # 初始化统计线程
        self.stats_thread = threading.Thread(target=self._print_stats, daemon=True)
        self.stats_thread.start()

        # 初始化内存监控线程
        self.memory_monitor = threading.Thread(target=self._monitor_memory, daemon=True)
        self.memory_monitor.start()

    def _send_request(self, url: str, method: str) -> Optional[bool]:
        """发送单个HTTP请求并处理重试"""
        retries = self.config.retries
        while retries >= 0:
            try:
                resp = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.config.timeout
                )
                resp.raise_for_status()
                with self.stats_lock:
                    self.success_count += 1
                return True
            except (RequestException, Exception) as e:
                logging.warning(f"Request failed: {str(e)}, retries left: {retries}")
                with self.stats_lock:
                    self.failure_count += 1
                retries -= 1
                if retries >= 0:
                    time.sleep(0.1)
        return False

    def _print_stats(self):
        """定期打印统计信息"""
        last_success = 0
        last_failure = 0
        while not self.stop_event.is_set():
            time.sleep(1)
            with self.stats_lock:
                current_success = self.success_count
                current_failure = self.failure_count
                qps = current_success - last_success
                error_rate = (current_failure - last_failure) / qps * 100 if qps > 0 else 0

                # 获取进程内存信息
                process = psutil.Process()
                mem_usage = process.memory_info().rss

                print(f"\rQPS: {qps:>5} | "
                      f"Success: {current_success:>6} | "
                      f"Failure: {current_failure:>6} | "
                      f"Error Rate: {error_rate:.2f}% | "
                      f"Memory: {mem_usage / 1024 / 1024:.2f}MB", end="")

                last_success, last_failure = current_success, current_failure

    def _monitor_memory(self):
        """内存监控线程"""
        while not self.stop_event.is_set():
            process = psutil.Process()
            current_mem = process.memory_info().rss

            if current_mem > self.memory_limit:
                logging.warning(
                    f"Memory limit exceeded: {current_mem / 1024 / 1024:.2f}MB > {self.config.memory_limit}MB")
                # 调整并发数（简单实现：减半）
                self.executor._max_workers = max(1, self.executor._max_workers // 2)
                logging.info(f"Adjusted max workers to: {self.executor._max_workers}")

            time.sleep(5)  # 每5秒检查一次

    def run(self):
        """启动压测"""
        futures = []
        try:
            for _ in range(self.config.total_requests):  # 使用 self.config.total_requests
                future = self.executor.submit(
                    self._send_request,
                    self.config.url,
                    self.config.method
                )
                futures.append(future)

                # 检查停止信号
                if self.stop_event.is_set():
                    break

        except KeyboardInterrupt:
            logging.info("Received interrupt signal, shutting down gracefully...")
        finally:
            self.stop_event.set()
            concurrent.futures.wait(futures)
            self.executor.shutdown(wait=False)
            print("\nShutdown completed.")


class Config:
    def __init__(self):
        parser = argparse.ArgumentParser(description="HTTP Stress Tester")
        parser.add_argument("-u", "--url", required=True, help="Target URL")
        parser.add_argument("-m", "--method", default="GET", choices=["GET", "POST"], help="HTTP method")
        parser.add_argument("-c", "--concurrency", type=int, default=10, help="Concurrency level")
        parser.add_argument("-n", "--total-requests", type=int, default=100, help="Total requests")  # 添加 total-requests 参数
        parser.add_argument("-t", "--timeout", type=float, default=5.0, help="Request timeout")
        parser.add_argument("-r", "--retries", type=int, default=3, help="Retry times")
        parser.add_argument("-ml", "--memory-limit", type=int, default=1024, help="Memory limit in MB")

        args = parser.parse_args()
        self.__dict__.update(args.__dict__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")
    config = Config()

    print("Starting stress test...")
    tester = StressTester(config)
    tester.run()

    # 最终统计
    with tester.stats_lock:
        total = tester.success_count + tester.failure_count
        print("\nFinal Report:")
        print(f"Total Requests: {total}")
        print(f"Successful: {tester.success_count} ({tester.success_count / total * 100}%)")
        print(f"Failed: {tester.failure_count} ({tester.failure_count / total * 100}%)")

# # 正常测试
# python question3.py -u https://www.baidu.com -c 10 -n 100
#
# # 模拟内存溢出（设置较低内存限制）
# python question3.py -u https://www.baidu.com -c 10 -n 10000 -ml 500
#
# # 模拟网络错误（使用无效URL）
# python question3.py -u http://nonexistent.example.com -c 20 -n 100 -r 5
