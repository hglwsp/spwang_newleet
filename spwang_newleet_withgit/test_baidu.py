import pytest
import yaml
import requests
import os


def load_test_cases(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        test_cases = yaml.safe_load(file)
    return [test_cases]  # 返回一个包含单个测试用例的列表


@pytest.mark.parametrize("test_case",
                         load_test_cases(os.path.join(os.path.expanduser('~'), 'Desktop', 'test_baidu.yaml')))
def test_baidu(test_case):
    # 执行请求
    request_step = test_case['steps'][0]['request']
    response = requests.request(
        method=request_step['method'],
        url=request_step['url']
    )

    # 提取响应数据
    status_code = response.status_code

    # 验证
    validate_step = test_case['steps'][2]['validate']['equals']
    for validation in validate_step.values():
        expected_status_code = validation[1]
        assert status_code == expected_status_code, f"Expected {expected_status_code}, but got {status_code}"
