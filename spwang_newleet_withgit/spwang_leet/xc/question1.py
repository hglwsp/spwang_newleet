import time
from functools import wraps

# 全局测试容器
tests = []


def test(func):
    """test装饰器：标记测试方法并注册到全局测试列表"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    tests.append(wrapper)
    return wrapper


def timed(func):
    """时间装饰器：统计测试方法执行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        wrapper.duration = end_time - start_time
        return result

    return wrapper


class TestResult:
    """测试结果记录类"""

    def __init__(self, test_func):
        self.test_func = test_func
        self.passed = False
        self.error = None
        self.start_time = None
        self.duration = 0.0

    def record_pass(self):
        self.passed = True
        self.duration = getattr(self.test_func, 'duration', 0.0) or (time.perf_counter() - self.start_time)

    def record_fail(self, error):
        self.passed = False
        self.error = str(error)
        self.duration = getattr(self.test_func, 'duration', 0.0) or (time.perf_counter() - self.start_time)


class TestRunner:
    """测试执行器"""

    def run(self, verbose=True):
        results = []

        # 执行所有测试
        for test_func in tests:
            result = TestResult(test_func)
            result.start_time = time.perf_counter()

            try:
                test_func()
                result.record_pass()
            except Exception as e:
                result.record_fail(e)

            results.append(result)

        # 生成报告
        self.generate_report(results, verbose)
        return results

    def generate_report(self, results, verbose=True):
        """生成格式化测试报告"""
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        failed = total - passed
        total_time = sum(r.duration for r in results)

        print("\n" + "=" * 50)
        print(f"{'Test Execution Report':^50}")
        print("=" * 50)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed} | Failed: {failed}")
        print(f"Total Duration: {total_time:.4f}s")

        if verbose:
            print("\n" + "-" * 50)
            print("{:<20} {:<10} {:<15}".format("Test Name", "Status", "Duration(s)"))
            print("-" * 50)
            for result in results:
                status = "PASSED" if result.passed else "FAILED"
                duration = f"{result.duration:.4f}"
                print("{:<20} {:<10} {:<15}".format(
                    result.test_func.__name__,
                    status,
                    duration
                ))

            if failed > 0 and verbose:
                print("\n" + "-" * 50)
                print("Failed Tests Details:")
                print("-" * 50)
                for result in results:
                    if not result.passed:
                        print(f"Test: {result.test_func.__name__}")
                        print(f"Error: {result.error}")
                        print(f"Duration: {result.duration:.4f}s\n")


# 断言方法
def assert_equal(expected, actual):
    """验证两个值是否相等"""
    if expected != actual:
        raise AssertionError(f"Expected {expected}, got {actual}")


def assert_raises(exception_type, func, *args, **kwargs):
    """验证函数是否抛出指定异常"""
    try:
        func(*args, **kwargs)
    except exception_type:
        return
    raise AssertionError(f"Expected {exception_type.__name__} to be raised")


# 测试验证代码
@test
@timed
def test_fast_math():
    """快速数学测试"""
    assert_equal(2 + 2, 4)
    time.sleep(0.1)  # 模拟耗时操作


@test
@timed
def test_slow_math():
    """慢速数学测试"""
    assert_equal(10 * 10, 100)
    time.sleep(0.3)


@test
@timed
def test_exception_handling():
    """异常处理测试"""
    assert_raises(ValueError, lambda: int("invalid"))


@test
def test_immediate_fail():
    """立即失败测试（无耗时统计）"""
    assert_equal(1, 2)


if __name__ == "__main__":
    runner = TestRunner()
    runner.run(verbose=True)