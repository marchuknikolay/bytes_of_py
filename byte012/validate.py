"""
Bite 12. Write a user validation function

Create a function that takes a username and checks for a valid user:
1. The username is in USERS,
2. the user is not expired, and
3. the user has the ADMIN role.

If those 3 conditions are met return SECRET.

If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist, UserAccessExpired and
UserNoPermission respectively. Check out the tests for more detail.

Have fun and keep calm and code in Python!
"""


from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here

def get_secret_token(username):
    pass
