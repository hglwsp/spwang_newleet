import requests

# 设置API密钥和请求参数
api_key = "sk-65ee7630e11c4a4eb40a156a6c6bf5c8"  # 替换为你的DeepSeek API密钥
url = "https://api.deepseek.com/generate_test_cases"  # DeepSeek API的URL
headers = {"Authorization": f"Bearer {api_key}"}
data = {
    "description": "测试用户登录功能，用户名是手机号，密码输入后可以隐藏。输入正确的用户名和密码后跳转到首页，输入错误给予对应提示。"
}

# 调用API
response = requests.post(url, headers=headers, json=data)
test_cases = response.json()

# 输出生成的测试用例
print("生成的测试用例:")
for test_case in test_cases:
    print(f"用例ID: {test_case['id']}")
    print(f"优先级: {test_case['priority']}")
    print(f"标题: {test_case['title']}")
    print(f"前置条件: {test_case['preconditions']}")
    print(f"步骤: {test_case['steps']}")
    print(f"预期结果: {test_case['expected_results']}")
    print()
