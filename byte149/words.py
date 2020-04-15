"""
Bite 149. Sorting words with constraint

Here is a list of words Jacob is trying to sort:

>>> words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
>>> sorted(words)

['2019', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'You', 'a', 'a', 'almost', 'and', 'and',
'wishes']

Hmm ... that year goes first. He actually wants words starting with a digit (first character) to go last!

Could you complete the function below to do this for him? So the result would be:

['a', 'a', 'almost', 'and', 'and', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'wishes', 'You',
'2019']

By the way, you can submit ideas/needs/wishes for Bites here. Cheers!

See you in the next Bite and keep calm and code in Python!

"""


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    pass
