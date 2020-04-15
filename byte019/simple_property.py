"""
Bite 19. Write a simple property

Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!
"""


from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expired_time):
        self.name = name
        self.expired_time = expired_time

    @property
    def expired(self):
        return datetime.now() > self.expired_time
