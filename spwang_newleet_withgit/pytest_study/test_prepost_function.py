# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_prepost_function.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 17:11
# @Copyright: 北京码同学

from spwang_newleet_withgit.requests_study.cookie_study import login, query


# 前置动作先完成登录
def setup_function():
    login(userName='shamo',password='123456')
    print('在每条用例开始前先执行我')
# 测试用例1：余额查询正确
def test_query():
    resp = query(userName='shamo')
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
# 测试用例2：用户不正确，查询失败
def test_query1():
    resp = query(userName='shamo1')
    # 针对接口响应做判断，做判断的过程就叫做断言
    # 判断响应状态码是否是200
    status_code = resp.status_code
    assert status_code == 200
    # 判断响应信息中的message是否是success
    message = resp.json()['message']
    assert message == '用户不合法'
    # 判断响应信息中的code是否是0
    code = resp.json()['code']
    assert code == '1'

# 后置处理器，所有用例执行完后清除数据
def teardown_function():
    print('在每条用例执行完后要做的事情，我来做')