"""
Bite 30. Movie data analysis

In this Bite we are going to parse a csv movie dataset to identify the directors with the highest rated movies:

1. Write get_movies_by_director: use csv.DictReader to convert movie_metadata.csv into a (default)dict of lists of Movie
namedtuples. Convert/filter the data: Only extract director_name, movie_title, title_year and imdb_score. Type
conversions: title_year -> int / imdb_score -> float Discard any movies older than 1960. Here is an extract:
....
{ 'Woody Allen': [
    Movie(title='Midnight in Paris', year=2011, score=7.7),
    Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
    Movie(title='To Rome with Love', year=2012, score=6.3),  ....
    ], ...
}

2. Write the calc_mean_score helper that takes a list of Movie namedtuples and calculates the mean IMDb score,
returning the score rounded to 1 decimal place.

3. Complete get_average_scores which takes the directors data structure
returned by get_movies_by_director (see 1.) and returns a list of tuples (director, average_score) ordered by highest
score in descending order. Only take directors into account with >= MIN_MOVIES
"""


import csv
from collections import defaultdict, namedtuple
import os
from statistics import mean
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    result = defaultdict(list)

    with open(MOVIE_DATA, newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            try:
                title_year = int(row['title_year'])

                if title_year > MIN_YEAR:
                    result[row['director_name']].append(
                        Movie(row['movie_title'], title_year, float(row['imdb_score'])))
            except ValueError:
                continue

    return result


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""

    return round(mean([movie.score for movie in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    result = []

    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            result.append((director, calc_mean_score(movies)))

    return sorted(result, key=lambda item: item[1], reverse=True)
