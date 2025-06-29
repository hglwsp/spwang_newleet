import requests
import json
from datetime import datetime


class LocalDeepSeekTestCaseGenerator:
    def __init__(self):
        self.base_url = "http://localhost:11434/api/generate"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.system_prompt = """
        你是一位专业的测试用例生成专家，需要遵循以下规则：
        1. 输出必须为严格的JSON格式
        2. 每个测试用例包含：用例ID、测试场景、前置条件、输入数据、预期结果
        3. 用例ID采用TC-四位数字格式（如TC-0001）
        4. 测试场景需覆盖正常流程和异常分支
        5. 输入数据需包含所有必要参数及其约束条件
        """

    def generate(self, requirement, model="deepseek-r1:1.5b"):
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": requirement}
            ],
            "stream": False
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=300
            )
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {str(e)}")
            return ""


def save_test_cases(test_cases, filename=None):
    if not filename:
        filename = f"test_cases_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)
    print(f"测试用例已保存至 {filename}")


def validate_test_cases(test_cases):
    errors = []
    for idx, case in enumerate(test_cases, 1):
        if not case["用例ID"].startswith("TC-"):
            errors.append(f"用例{idx}: 无效的ID格式")
        if "预期结果" not in case:
            errors.append(f"用例{idx}: 缺少预期结果")
        if not case.get("输入数据"):
            errors.append(f"用例{idx}: 缺少输入数据")
    return errors


# 示例用法
if __name__ == "__main__":
    # 初始化生成器
    generator = LocalDeepSeekTestCaseGenerator()

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

    # 生成测试用例
    raw_response = generator.generate(requirement)
    test_cases = json.loads(raw_response)

    # 验证并保存结果
    if test_cases:
        validation_errors = validate_test_cases(test_cases)
        if validation_errors:
            print("发现测试用例格式错误：")
            for err in validation_errors:
                print(f"- {err}")
        else:
            save_test_cases(test_cases)