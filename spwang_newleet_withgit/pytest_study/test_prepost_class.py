# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_prepost_class.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/10 17:15
# @Copyright: 北京码同学
from spwang_newleet_withgit.requests_study.cookie_study import query, login


class TestQuery:
    #类级别前置
    def setup_class(self):
        print('在当前类下测试开始前执行我')
        login(userName='shamo',password='123456')
        print('在当前类下测试开始前执行我')
    # 类级别后置
    def teardown_class(self):
        print('在当前类下所有测试完成后执行我')

    # 方法级别的前置
    def setup_method(self):
        print('每个测试用例执行前执行我')
    # 方法的后置
    def teardown_method(self):
        print('每个测试用例执行后执行我')

    # 测试用例1：余额查询正确
    def test_query(self):
        resp = query(userName='shamo')
        # 针对接口响应做判断，做判断的过程就叫做断言
        # 判断响应状态码是否是200
        status_code = resp.status_code
        assert status_code != 200
        # 判断响应信息中的message是否是success
        message = resp.json()['message']
        assert message == 'success'
        # 判断响应信息中的code是否是0
        code = resp.json()['code']
        assert code == '0'

    # 测试用例2：用户不正确，查询失败
    def test_query1(self):
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