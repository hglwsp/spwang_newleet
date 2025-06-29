import requests
import time
import json

from IPython.core.debugger import prompt


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
        prompt = """
                你是一位专业的测试用例生成专家，需要遵循以下规则：
                1. 输出必须为严格的JSON格式
                2. 每个测试用例包含：用例ID、测试场景、前置条件、输入数据、预期结果
                3. 用例ID采用TC-四位数字格式（如TC-0001）
                4. 测试场景需覆盖正常流程和异常分支
                5. 输入数据需包含所有必要参数及其约束条件
                """

        system_message = """
        你是一位专业的测试用例编写专家，能够根据需求精确生成高质量的测试用例。
        重要规则：
        1. 确保每个用例ID唯一，避免重复
        2. 采用清晰的Markdown格式输出
        3. 确保测试用例覆盖关键功能路径和边界条件
        输出格式：
        ```markdown
        ## 测试用例集
        ### 用例ID：[模块]_[功能]_[序号]
        **优先级**：P0/P1/P2/P3
        **标题**：简明描述测试目的
        **前置条件**：
        - 条件1
        - 条件2
        **步骤**：
        1. 第一步
        2. 第二步
        **预期结果**：
        - 具体的预期结果
        [重复上述模板直到达到指定的用例数量]
        ## 总结
        - 测试覆盖度：描述测试覆盖的方面
        - 建议：任何关于测试执行的建议
        """

        userfirstinput = input("You: ")
        user_input = system_message + userfirstinput
        print(user_input)
        if userfirstinput.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        payload = {
            "model": "deepseek-r1:7b",
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


