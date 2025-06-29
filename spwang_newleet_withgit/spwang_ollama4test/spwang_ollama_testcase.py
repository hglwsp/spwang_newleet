import requests
import json

def chat_with_ai(requirement):
    history = []
    url = "http://localhost:11434/api/generate"
    while True:
        # user_input = input("You: ")
        # if user_input.lower() in ["exit", "quit"]:
        #     print("Exiting chat...")
        #     break
        system_prompt = """
                你是一位专业的测试用例生成专家，需要遵循以下规则：
                1. 输出必须为严格的JSON格式
                2. 每个测试用例包含：用例ID、测试场景、前置条件、输入数据、预期结果
                3. 用例ID采用TC-四位数字格式（如TC-0001）
                4. 测试场景需覆盖正常流程和异常分支
                5. 输入数据需包含所有必要参数及其约束条件
                """
        payload = {
            "model": "deepseek-r1:latest",
            # "prompt": user_input,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": requirement}
            ],
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

            history.append(requirement)
            history.append(ai_response)
        except Exception as e:
            print("******************.")
            print(f"An error occurred: {e}")
            print(f"Response: {response.text}")

if __name__ == "__main__":
    print("Welcome to the AI Chatbot!")
    # 定义测试需求
    requirement = """
    测试对象：航班预订系统
    功能描述：
    - 支持单程/往返机票查询
    - 价格显示需含税费（总价=票价+燃油费+机场税）
    - 婴儿票（0-2岁）价格为成人票10%
    - 改签规则：起飞前24小时外免费改签
    业务规则：
    - 同一乘客同航班只能预订一张票
    - 信用卡支付需验证CVV码
    - 积分兑换需至少10000积分
    """
    chat_with_ai(requirement)


