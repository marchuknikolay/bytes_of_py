"""
Bite 47. Write a new password field validator

You know these Create a new password forms? They do a lot of checks to make sure you make a password that is hard to
guess and you will surely forget.

In this Bite you will write a validator for such a form field.

Complete the validate_password function below. It takes a password str and validates that it:
1. is between 6 and 12 chars long (both inclusive)
2. has at least 1 digit [0-9]
3. has at least two lowercase chars [a-z]
4. has at least one uppercase char [A-Z]
5. has at least one punctuation char (use: PUNCTUATION_CHARS)
6. Has not been used before (use: used_passwords)

If the password matches all criteria the function should store the password in used_passwords and return True.

Have fun, keep calm and code in Python!
"""


import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    pass
