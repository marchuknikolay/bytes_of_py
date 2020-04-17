"""
Bite 18. Find the most common word

Write a function that returns the most common (non stop)word in this Harry Potter text.

Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords. Your function should return
a tuple of (most_common_word, frequency).

The template code already loads the Harry Potter text and list of stopwords in.

Check the tests for more info - have fun!
"""


import os
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    pass
