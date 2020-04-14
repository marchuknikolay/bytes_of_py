"""
Bite 80. Check equality of two lists

In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) according to
the type of equality of the lists:
1. return SAME_REFERENCE if both lists reference the same object,
2. return SAME_ORDERED if they have the same content and order,
3. return SAME_UNORDERED if they have the same content unordered,
4. return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
5. and finally return NO_EQUALITY if none of the previous cases match.

Have fun and keep calm and code in Python!
"""


from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    pass
