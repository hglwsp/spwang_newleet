# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : file_upload.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 16:10
# @Copyright: 北京码同学


import requests

host = 'http://82.156.74.26:9088'

# 使用requests库中的session对象发起接口调用，可以自动管理cookie传递
session = requests.session()
def upload_file():
    url = f'{host}/pinter/file/api/upload'
    # 文件参数
    files = {
        'file':open(file=r'C:\Users\lixio\Desktop\login.txt',mode='rb')
    }
    # 发起接口调用
    resp = session.post(url=url,files=files)
    print(resp.text)
if __name__ == '__main__':
    upload_file()