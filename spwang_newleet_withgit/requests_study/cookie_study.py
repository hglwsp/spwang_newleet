# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : cookie_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 15:34
# @Copyright: 北京码同学


import requests

host = 'http://82.156.74.26:9088'

# 使用requests库中的session对象发起接口调用，可以自动管理cookie传递
session = requests.session()
def login(userName='shamo',password='123456'):
    # 准备接口数据
    url = f'{host}/pinter/bank/api/login'
    # 表单参数
    data = {
        "userName":userName,
        "password": password
    }
    # 发起接口调用
    resp = session.post(url=url,data=data)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')

    # 获取响应报文数据
    # 以字符串的格式得到响应报文数据
    text = resp.text
    print(f'响应内容字符串：{text}')
    json = resp.json() # 以json格式数据得到结果，在python中拿到的就是字典类型
    print(f'响应内容json：{json}')
    return resp

def query(userName='shamo'):
    # 准备接口数据
    url = f'{host}/pinter/bank/api/query'
    # 查询参数
    params = {
        "userName":userName
    }
    # 发起接口调用
    resp = session.get(url=url,params=params)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')

    # 获取响应报文数据
    # 以字符串的格式得到响应报文数据
    text = resp.text
    print(f'响应内容字符串：{text}')
    json = resp.json() # 以json格式数据得到结果，在python中拿到的就是字典类型
    print(f'响应内容json：{json}')
    return resp
if __name__ == '__main__':
    login()
    query()