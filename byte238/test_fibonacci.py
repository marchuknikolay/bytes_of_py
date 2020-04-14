"""
Bite 238. Write tests for Fibonacci

Our first Test Bite! The concept is simple: to pass a Test Bite, you write tests for the program under the "Code to
Test" tab. We run MutPy against your code to see if your tests are strong enough.

To kick this off we have you write some tests for fib which generates a Fibonacci sequence. Good luck and let us know
if you have any feedback.
"""


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
