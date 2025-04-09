# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : get_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 15:04
# @Copyright: 北京码同学
import requests

host = 'http://82.156.74.26:9088'

def get():

    # 你要针对一个接口发起调用，先要准备这个接口请求数据
    url = f'{host}/pinter/com/getSku'
    # headers 头信息一般我们不用关注，除非本身有特殊信息
    # 请求参数定义
    params = {
        "id":1
    }
    # 上面已经准备好了接口数据，接下来该发起调用了
    # resp代表接口发起后，服务器返回的数据对象
    # resp对象包括了响应状态码、响应头信息、响应body报文
    resp = requests.get(url=url,params=params)
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
    get()