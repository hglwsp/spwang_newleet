import pytest

import time

from pytest_assume.plugin import assume


@pytest.fixture(scope="function")
def fix():
    print("fixture1")
    yield time.time()
    print("fixture2")

test_data = [
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 7)
]


@pytest.mark.parametrize("x, y, expected",test_data)
def test_add(x, y, expected):
    # assert x + y == expected
    assume (x+y) == expected
    print("#################################")
    c = 0
    assert c == 2


p1 = [1,2,3]
p2 = [4,5,-2]


# @pytest.mark.parametrize("x",p1)
# @pytest.mark.parametrize("y",p2)
# def test_pult(x,y):
#     # pytest.assume(x>0)
#     assert x*y > 100
#     # print("#################################")

def test_example():
    x = 5

    y = 10

    pytest.assume(x == y)  # 第一个断言

    pytest.assume(x > y)  # 第二个断言

    pytest.assume(x % 2 == 0)  # 第三个断言

