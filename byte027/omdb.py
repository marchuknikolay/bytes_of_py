"""
Bite 27. Parse omdb movie json data

Working with APIs is very common these days and lucky for us they increasingly return JSON (over XML). We saved OMDb
responses for some cool movies into a file that the tests load in.

Parse this data answering some questions:
1. get_movie_data consumes a list of movie json files (1 movie per file), returning a list of movie dicts, so for each
movie you convert the json file to a dict.
2. now you have the data structure, loop through the movies and return the movie:
    - with Comedy in Genres (get_single_comedy)
    - that had the most nominations (get_movie_most_nominations)
    - having the longest runtime (get_movie_longest_runtime)

Expect to do some string parsing and type conversions here. We hope you like it, enjoy!
"""


import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    pass


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    pass


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    pass


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    pass
