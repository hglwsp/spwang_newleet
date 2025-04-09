# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : put_delete_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 15:29
# @Copyright: 北京码同学
import requests

host = 'http://82.156.74.26:9088'
def put():
    # 整理测试数据
    url = f'{host}/pinter/com/phone'
    json = 	{"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}
    resp = requests.put(url=url,json=json)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')

    # 获取响应报文数据
    # 以字符串的格式得到响应报文数据
    text = resp.text
    print(f'响应内容字符串：{text}')
    json = resp.json() # 以json格式数据得到结果，在python中拿到的就是字典类型
    print(f'响应内容json：{json}')
def delete():
    # 整理测试数据
    url = f'{host}/pinter/com/phone'
    json = 	{"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}
    resp = requests.delete(url=url,json=json)
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
    put()
    delete()
