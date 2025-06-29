from string import Template

# 定义模板
template = Template('Hello, ${name}! You are ${age} years old.')

# 替换占位符
data = {'name': 'Alice', 'age': 30}
result = template.substitute(data)

print(result)  # 输出: Hello, Alice! You are 30 years old.


name = "Bob"
age = 25

# 使用 f-string 格式化
result = f"Hello, {name}! You are {age} years old."
print(result)  # 输出: Hello, Bob! You are 25 years old.
