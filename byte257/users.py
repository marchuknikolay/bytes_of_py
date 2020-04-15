"""
Bite 257. Extract users dict from a multiline string

A quick Bite to practice some string parsing extracting a users dict from a password file.

Complete get_users is how it works:

>>> from users import get_users
>>> pw = ""
... postfix:x:108:112::/var/spool/postfix:/bin/false
... ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
... artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
... ""
>>> get_users(pw)
{'postfix': 'unknown', 'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}

So keys are usernames, values are names. Note that commas inside the name get replace by a single space. Trailing commas
(not in this example) get stripped off.

Have fun and keep calm and code in Python!
"""


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    pass
