"""
Bite 44. License key generator

Write a function called gen_key that creates a license key with this format: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

The key consists of a combination of upper case letters and digits.

It takes two arguments: parts and chars_per_part which default to 4 and 8 respectively, so you can call the function
like:

gen_key() to get a similar key as above, or
as gen_key(parts=3, chars_per_part=4) to get a shorter one, e.g. 54N8-I70K-2JZ7
Before you default to random, check if Python >= 3.6 has a better option available for this task ...
"""

import random
import string


def gen_key(parts=4, chars_per_part=8):
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=chars_per_part))
                    for _ in range(parts))
