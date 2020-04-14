"""
Bite 96. Build Unix' wc program in Python

In this Bite you will convert Unix' wc command into Python. Your function takes a file (absolute path), reads it in
and calculates the lines/words/chars. It returns a string of these numbers and the filename, like as a typical wc
output, for example:

# Unix command
$ wc wc.py
      22      85     771 wc.py

# your script
$ python wc.py  wc.py
22	85	771 wc.py

Don't worry about the amount of white space between the columns, you can use tabs or spaces.

Unix files add an extra newline to the end so for content Hello\nworld Unix' wc would return 12 (not 11):

$ cat hello
hello
world
$ wc hello
       2       2      12 hello

As this is a Beginner Bite we can save you some head aches by suggesting you to use splitlines for the line counts!

See the tests for more info. Thanks Brian for introducing us to pytest's tmp_path fixture!

Have fun and keep coding in Python!
"""


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    pass


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
