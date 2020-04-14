import pytest

from byte238.fibonacci import fib


def test_negative_value():
    with pytest.raises(ValueError):
        fib(-1)


def test_zero_one():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55
