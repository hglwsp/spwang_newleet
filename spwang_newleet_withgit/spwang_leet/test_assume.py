import pytest

def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5  # 断言结果
    assert add(-1, 1) == 0