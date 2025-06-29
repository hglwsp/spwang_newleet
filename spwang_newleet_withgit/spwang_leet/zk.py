
# 输入数字类型
# num = input("数字：")
# print("原类型：", type(num), "结果：", num)
# num = float(num)
# print("转换后的类型：", type(num), "结果：%.2f" % num)


num = input("数字：")
print("原类型：", type(num), "结果：", num)
num = float(num)
print("转换后的类型：", type(num), "结果：", num)  # 打印未格式化的值
formatted_num = "%.2f" % num
print("格式化后的结果：", formatted_num)