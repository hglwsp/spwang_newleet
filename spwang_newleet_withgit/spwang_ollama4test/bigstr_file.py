def find_longest_line(file_path):
    longest_line = ""
    max_length = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行末的换行符
            stripped_line = line.strip()
            if len(stripped_line) > max_length:
                max_length = len(stripped_line)
                longest_line = stripped_line

    return longest_line


# 示例使用
file_path = 'your_file.txt'  # 替换为你的文件路径
longest_line = find_longest_line(file_path)
print("最长的一行是：", longest_line)

def find_longest_line(file_path):
    longest_str = ""
    max_length = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if len(stripped_line) > max_length:
                max_length = len(stripped_line)
                longest_str = stripped_line
    return longest_str