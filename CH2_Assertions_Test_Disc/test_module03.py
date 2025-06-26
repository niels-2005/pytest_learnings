import pytest


def test_case1():
    with pytest.raises(Exception):
        assert 1 / 0


def func1(a, b):
    if a > b:
        raise Exception("meow")


def test_case2():
    with pytest.raises(Exception) as excinfo:
        func1(2, 1)
    assert (str(excinfo.value)) == "meow"
