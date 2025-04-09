import requests
import time
import json

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        print("start...")
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
    print("Welcome to the AI Chatbot for test!")
    print("Type 'exit' or 'quit' to end the chat.")
    chat_with_ai()
"""
根据提供的接口信息，生成接口测试用例，并以json格式返回。
json格式需包含请求体、请求头。接口信息如下：
{
  "基础信息": {
    "customerId": "字符串", // 客户 ID
    "orderId": "字符串" // 订单唯一标识符
  },
  
  "商品信息": {
    "productTitle": "字符串", // 商品标题
    "productName": "字符串", // 商品名称
    "size": "字符串", // 商品尺寸
    "quantity": 数字 // 商品数量
  },
  
  "订单基本信息": {
    "orderStartTime": "字符串", // 订单开始时间（如YYYY-MM-DD HH:mm:ss）
    "estimatedTime": "字符串" // 预计完成时间
  },
  
  "支付信息": {
    "paymentMethod": "字符串", // 支付方式（如信用卡、美元等）
    "paymentAmount": 数字, // 支付金额
    "paymentType": "字符串" // 支付类型（如在线支付、支票等）
  },
  
  "配送信息": {
    "ship_to_address": 地址对象, // 发货地址
    "deliveryTime": "字符串", // 预计送达时间
    "运费选项": 数组 // 运费选项描述
  },
  
  "优惠/折扣": {
    "availableCoupons": 数组 // 可用优惠券列表
  },
  
  "订单附加": {
    "isBulkOrder": 布尔值, // 是否为批量订单
    "totalInBatch": 数字, // 批量商品总价
    "priceWithoutTax": 数字 // 不包含税费的总金额
  },
  
  "额外选项": {
    "includeInvoice": 布尔值, // 是否生成发票
    "trackId": "字符串", // 跟踪号
    "returnPolicy": "字符串" // 退货政策描述
  }
}
"""
