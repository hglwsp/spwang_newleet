# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_func_case.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 16:25
# @Copyright: 北京码同学



from spwang_newleet_withgit.requests_study.cookie_study import login

# 测试用例1：用户名密码正确
def test_login():
    # 调用封装好的登录接口函数，传递测试数据，拿到接口响应对象
    resp = login(userName='shamo',password='123456')
    print(type(resp))
    # 针对接口响应做判断，做判断的过程就叫做断言
    # 判断响应状态码是否是200
    status_code = resp.status_code
    assert status_code == 200
    # 判断响应信息中的message是否是success
    message = resp.json()['message']
    assert message == 'success'
    # 判断响应信息中的code是否是0
    code = resp.json()['code']
    assert code == '0'

# 测试用例2：用户名为空，密码正确
def test_login_userisnull():
    # 调用封装好的登录接口函数，传递测试数据，拿到接口响应对象
    resp = login(userName='',password='123456')
    # 针对接口响应做判断，做判断的过程就叫做断言
    # 判断响应状态码是否是200
    status_code = resp.status_code
    assert status_code == 200
    # 判断响应信息中的message是否是success
    message = resp.json()['message']
    assert message == '参数为空'
    # 判断响应信息中的code是否是0
    code = resp.json()['code']
    assert code == '1'