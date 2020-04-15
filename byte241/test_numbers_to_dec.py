"""
Bite 241. Write tests for list_to_decimal

Our 4th test Bite. Michael made a calculator that will be able to accept a list of decimal digits and returns an
integer where each int of the given list represents decimal place values from first element to last.

He wrote the function in such a way that it only accepts positive digits in range(0, 10) and anything that is not
raises a ValueError if its out of range, or a TypeError if its not an int type.

Some examples:

[0, 4, 2, 8] => 428
[1, 2] => 12
[3] => 3
[6, 2, True] => raises TypeError
[-3, 12] => raises ValueError
[3.6, 4, 1] => raises TypeError
['4', 5, 3, 1] => raises TypeError

In this Bite you are tasked to write the tests for this function. Good luck and keep calm and code in Python!
"""


from typing import List


def list_to_decimal(nums: List[int]) -> int:
    """Accept a list of positive integers in the range(0, 10)
       and return a integer where each int of the given list represents
       decimal place values from first element to last.  E.g
        [1,7,5] => 175
        [0,3,1,2] => 312
        Place values are 10**n where n represents the digit position
        Eg to calculate 1345, we have 5 1's, 4 10's, 3 100's and 1 1000's
        1,     3  ,  4  , 5
        1000's, 100's, 10's, 1's
    """
    for num in nums:
        if isinstance(num, bool) or not isinstance(num, int):
            raise TypeError
        elif not num in range(0, 10):
            raise ValueError

    return int(''.join(map(str, nums)))
