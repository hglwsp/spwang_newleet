import requests
import time
import json

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        print("Starting function execution...")
        result = func(*args, **kwargs)  # 执行原函数
        end_time = time.time()  # 记录结束时间
        print("end...")
        elapsed_time = end_time - start_time  # 计算耗时
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

@time_decorator
def chat_with_ai():
    history = []
    url = "http://localhost:11434/api/generate"
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        payload = {
            "model": "deepseek-r1:latest",
            "prompt": user_input,
            "options": {
                "temperature": 0.8,
                "max_tokens": 512,
                "top_p": 0.9
            },
            "stream": True
        }

        response = requests.post(url, json=payload, stream=True)
        print("I'm thinking...")

        # 检查响应状态码
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            continue

        # 检查响应内容类型
        content_type = response.headers.get('content-type', '')
        if 'application/json' not in content_type and 'application/x-ndjson' not in content_type:
            print(f"Unexpected content type: {content_type}")
            print(f"Response: {response.text}")
            continue

        try:
            ai_response = ""
            for line in response.iter_lines():
                if line:
                    chunk_data = line.decode('utf-8')
                    chunk_json = json.loads(chunk_data)
                    ai_response += chunk_json.get('response', '')  # 假设每个 JSON 对象包含 'response' 字段
                    # print(f"AI: {chunk_json.get('response', '')}", end='', flush=True)

            print()  # 添加换行符以便于阅读
            print(f"AI (complete): {ai_response}")

            history.append(user_input)
            history.append(ai_response)
        except Exception as e:
            print("******************.")
            print(f"An error occurred: {e}")
            print(f"Response: {response.text}")

if __name__ == "__main__":
    print("Welcome to the AI Chatbot!")
    chat_with_ai()
