# try:
#     with open('file4.txt', 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
#     # with open('file3.txt', 'w') as f:
#     #     f.write('Hello, World!')
#     #     print(f.read())
#
#
# try:
#     print(1/0)
# except (NameError,ZeroDivisionError) as e:
#     print(e)
#     print('有错误')

try:
    with open('file4.txt', 'r') as f:
        print(f.read())
    print(1/0)
except FileNotFoundError as e:
    print(e)
    with open('file4.txt', 'w') as f:
        f.write('Hello, llzzmm!')
        print("文件已创建")
    with open('file4.txt', 'r') as f:
        print(f.read())
except ZeroDivisionError as e:
    print(e)
    print('有错误')
    print(2/1)
