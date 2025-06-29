import ollama

try:
    response = ollama.chat(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "system", "content": "你是测试专家"},
            {"role": "user", "content": "测试支付功能"}
        ]
    )
    print("验证成功:", response.response)
except Exception as e:
    print("验证失败:", str(e))