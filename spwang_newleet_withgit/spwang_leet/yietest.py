# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
# # 创建生成器对象
# generator = countdown(5)
#
# # 通过迭代生成器获取值
# print(next(generator))  # 输出: 5
# print(next(generator))  # 输出: 4
# print(next(generator))  # 输出: 3
#
# # 使用 for 循环迭代生成器
# print(generator)
# for value in generator:
#     print(value)  # 输出: 2 1

list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print(next(it))   # 输出迭代器的下一个元素
print(next(it))

