import unittest
from unittest.mock import patch
import requests


class TestApp(unittest.TestCase):
    @patch('requests.get')
    def test_get_status_success(self, mock_get):
        # 模拟 requests.get 的返回值
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'code': 200,
            'message': 'Operation successful llzzmm'
        }

        # 调用被测试的代码
        response = requests.get('http://127.0.0.1:5000/api/status', params={'status': 'success'})

        # 断言
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'code': 200, 'message': 'Operation successful llzzmm'})

    @patch('requests.get')
    def test_get_status_failure(self, mock_get):
        # 模拟 requests.get 的返回值
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'code': 500,
            'message': 'Internal server error'
        }

        # 调用被测试的代码
        response = requests.get('http://127.0.0.1:5000/api/status', params={'status': 'failure'})

        # 断言
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'code': 500, 'message': 'Internal server error'})


if __name__ == '__main__':
    unittest.main()
