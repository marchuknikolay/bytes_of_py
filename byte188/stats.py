"""
Bite 188. Get statistics from PyBites test code

Did you know Python has a statistics module?

For this Bite we did a line count on our test code for 186 Bites, running this command: wc -l */test_*.py|sort -n
-k2|grep -v total > testfiles_number_loc.txt. Output:

$ head -5 testfiles_number_loc.txt
      13 01/test_numbers.py
      17 02/test_regex.py
      23 03/test_wordvalue.py
      15 04/test_tags.py
      21 05/test_names.py
       ...

Complete the stats dict wih all the relevant metrics producing the following output:

Basic statistics:
- count     :     186
- min       :       6
- max       :     337
- mean      :   43.74

Population variance:
- pstdev    :   43.04
- pvariance : 1852.39

Estimated variance for sample:
- count     :   93.00
- stdev     :   30.24
- variance  :  914.36

We already did the formatting for you, so just focus on completing stats using a combination of Python builtins and
the statistics module.

We retrieved this example from Python 3 Module of the Week (link provided upon resolving this Bite ...)

Make sure you check out statistics docs while coding this Bite. Other than that, keep calm and code some stats in
Python!
"""


import os
import statistics
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'testfiles_number_loc.txt'
STATS = os.path.join(TMP, DATA)
if not os.path.isfile(STATS):
    urlretrieve(os.path.join(S3, DATA), STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    pass


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(count=None,
                 min_=None,
                 max_=None,
                 mean=None,
                 pstdev=None,
                 pvariance=None,
                 sample_count=None,
                 sample_stdev=None,
                 sample_variance=None,
                 )

    return STATS_OUTPUT.format(**stats)
