# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : post_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 15:19
# @Copyright: 北京码同学
import requests

host = 'http://82.156.74.26:9088'
def post_form():
    # 准备接口数据
    url = f'{host}/pinter/com/login'
    # 表单参数
    data = {
        "userName":'shamo',
        "password": 123456
    }
    # 发起接口调用
    resp = requests.post(url=url,data=data)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')

    # 获取响应报文数据
    # 以字符串的格式得到响应报文数据
    text = resp.text
    print(f'响应内容字符串：{text}')
    json = resp.json() # 以json格式数据得到结果，在python中拿到的就是字典类型
    print(f'响应内容json：{json}')

def post_json():
    # 准备接口数据
    url = f'{host}/pinter/com/register'
    json = 	{"userName":"test",
               "password":"1234","gender":1,
               "phoneNum":"110",
               "email":"beihe@163.com",
               "address":"Beijing"}
    # 发起调用
    resp = requests.post(url=url,json=json)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')

    # 获取响应报文数据
    # 以字符串的格式得到响应报文数据
    text = resp.text
    print(f'响应内容字符串：{text}')
    json = resp.json() # 以json格式数据得到结果，在python中拿到的就是字典类型
    print(f'响应内容json：{json}')
if __name__ == '__main__':
    post_form()
    post_json()