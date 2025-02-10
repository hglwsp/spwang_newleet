from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/status', methods=['GET'])
def get_status():
    # 从查询参数中获取 status 值，默认为 'success'
    status_code = request.args.get('status', 'success')

    # 根据 status 值设置响应数据
    response_data = {
        'code': 200 if status_code == 'success' else 500,
        'message': 'Operation successful' if status_code == 'success' else 'Internal server error'
    }

    # 如果需要，可以根据 status_code 设置 HTTP 响应状态码
    # 但通常，对于 RESTful API，我们会在响应体中明确指定 code，而不是改变 HTTP 状态码
    # 除非有特定的 HTTP 状态码需要返回（如 404 Not Found, 400 Bad Request 等）
    # 下面这行代码是注释状态，因为它会覆盖 Flask 的默认行为（通常返回 200 OK）
    # return jsonify(response_data), response_data['code']

    # 直接返回 JSON 响应
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)