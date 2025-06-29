import yaml
import re
import csv
import json
import random
from string import ascii_letters, digits
from typing import List, Dict, Any


class DataGenerator:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)
        self.generators = {
            'random_string': self.generate_random_string,
            'random_email': self.generate_random_email,
            'random_integer': self.generate_random_integer
        }

    def load_config(self, path: str) -> List[Dict]:
        """加载yaml rules"""
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)['fields']

    def generate_data(self, num_records: int = 10, include_boundary: bool = True) -> List[Dict]:
        """生成测试数据"""
        data = []
        for _ in range(num_records):
            record = {}
            for field in self.config:
                value = self.generate_field_value(field, include_boundary)
                record[field['name']] = value
            data.append(record)
        return data

    def generate_field_value(self, field: Dict, include_boundary: bool) -> Any:
        """生成单个字段值"""
        if include_boundary and random.random() < 0.2:  # 20%概率生成边界值
            return self.generate_boundary_value(field)
        return self.generate_normal_value(field)

    def generate_normal_value(self, field: Dict) -> Any:
        """生成正常值"""
        generator = self.generators[field['generator']]
        return generator(field)

    def generate_boundary_value(self, field: Dict) -> Any:
        """生成边界值"""
        if field['type'] == 'string' and field['generator'] == 'random_string':
            return self.generate_boundary_string(field)
        elif field['type'] == 'integer':
            return random.choice([field['min_value'], field['max_value']])
        elif field['type'] == 'string' and field['generator'] == 'random_email':
            return self.generate_random_email(field)
        return None

    def generate_random_string(self, field: Dict) -> str:
        length = random.randint(field['min_length'], field['max_length'])
        return ''.join(random.choices(ascii_letters, k=length))

    def generate_random_email(self, field: Dict) -> str:
        username = ''.join(random.choices(ascii_letters + digits, k=8))
        domain = f"{random.choice(['gmail', 'yahoo', 'hotmail'])}.com"
        return f"{username}@{domain}"

    def generate_random_integer(self, field: Dict) -> int:
        return random.randint(field['min_value'], field['max_value'])

    def generate_boundary_string(self, field: Dict) -> str:
        """生成字符串边界值"""
        choices = [
            ''.join(random.choices(ascii_letters, k=field['min_length'])),
            ''.join(random.choices(ascii_letters, k=field['max_length']))
        ]
        return random.choice(choices)

    def validate_data(self, data: List[Dict]) -> bool:
        """验证数据格式"""
        for record in data:
            for field in self.config:
                value = record[field['name']]
                if not re.fullmatch(field['regex'], str(value)):
                    print(f"验证失败: {field['name']} = {value}")
                    return False
        return True

    def export_csv(self, data: List[Dict], filename: str):
        """导出CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[f['name'] for f in self.config])
            writer.writeheader()
            writer.writerows(data)

    def export_json(self, data: List[Dict], filename: str):
        """导出JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # 使用示例
    dg = DataGenerator('config.yaml')
    test_data = dg.generate_data(num_records=5, include_boundary=True)

    print("生成数据预览:")
    print(json.dumps(test_data, indent=2, ensure_ascii=False))

    if dg.validate_data(test_data):
        print("\n数据验证通过")
        dg.export_csv(test_data, 'output.csv')
        dg.export_json(test_data, 'output.json')
        print("数据已导出到CSV和JSON文件")
    else:
        print("\n数据验证失败")