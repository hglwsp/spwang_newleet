# client_requests.py
import requests

# Flask 应用的 URL
url = 'http://127.0.0.1:5000/api/status'

# 发送 GET 请求，带有 status=success 查询参数
response = requests.get(url, params={'status': 'success'})
print('Success Response:')
print(response.status_code)  # 应该打印 200，因为这是 Flask 的默认 HTTP 状态码（尽管我们在响应体中指定了 code: 200）
print(response.json())       # 应该打印 {'code': 200, 'message': 'Operation successful'}

# 发送 GET 请求，带有 status=error 查询参数
response = requests.get(url, params={'status': 'error'})
print('Error Response:')
print(response.status_code)  # 同样应该打印 200，因为 Flask 默认返回 200 OK
print(response.json())       # 应该打印 {'code': 500, 'message': 'Internal server error'}