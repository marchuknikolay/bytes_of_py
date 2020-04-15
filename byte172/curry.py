"""
Bite 172. Having fun with Python Partials

Meet another gem in the standard library: functools, which contains tools for functional-style programming.

In this Bite you will play with its useful partial() function which -as per PEP 309- lets you construct variants of
existing functions that have some of the parameters filled in.

The PEP also shows a small but realistic example:

import functools

def log (message, subsystem):
    "Write the contents of 'message' to the specified subsystem."
    print '%s: %s' % (subsystem, message)
    ...

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')

In this Bite you will apply this concept to the round builtin:

>>> round(10.42342, 2)
10.42

Write two partials to add the default behavior of rounding to 0 and 4 places respectively. See the template code
below ...

Good luck and keep calm and code in Python!
"""


from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
# rounder_int =  # you code
# rounder_detailed =  # you code
