# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : token_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 15:55
# @Copyright: 北京码同学


import requests

host = 'http://82.156.74.26:9088'

# 使用requests库中的session对象发起接口调用，可以自动管理cookie传递
session = requests.session()
def login(userName='shamo',password='123456'):
    # 准备接口数据
    url = f'{host}/pinter/bank/api/login2'
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
    """
    {
        "code": "0",
        "message": "success",
        "data": "7a8b506d176a4bdea7c60123a7264e62"
    }
    """
    # 从登录接口响应中提取data字段，作为token值
    global token
    token = json['data']
    return resp

def query():
    # 准备接口数据
    url = f'{host}/pinter/bank/api/query2'
    headers = {
        "testfan-token":token
    }
    # 查询参数
    params = {
        "userName":'shamo'
    }
    # 发起接口调用
    resp = session.get(url=url,params=params,headers=headers)
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
    login()
    query()