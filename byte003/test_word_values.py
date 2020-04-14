from unittest import TestCase

from byte003.word_values import load_words, calc_word_value, max_word_value


class Test(TestCase):
    def setUp(self):
        self.words = load_words()

    def test_load_words(self):
        self.assertEqual(list, type(self.words))
        self.assertEqual(235886, len(self.words))
        self.assertEqual('A', self.words[0])
        self.assertEqual('Zyzzogeton', self.words[-1])
        self.assertTrue(' ' not in ''.join(self.words))

    def test_calc_word_value(self):
        self.assertEqual(7, calc_word_value('bob'))
        self.assertEqual(13, calc_word_value('JuliaN'))
        self.assertEqual(14, calc_word_value('PyBites'))
        self.assertEqual(56, calc_word_value('benzalphenylhydrazone'))

    def test_max_word_value(self):
        self.assertEqual('barbeque', max_word_value(['bob', 'julian', 'pybites', 'quit', 'barbeque']))
        self.assertEqual('benzalphenylhydrazone', max_word_value(self.words[20000:21000]))

    def test_non_scrabble_characters(self):
        self.assertEqual('a', max_word_value(['a', 'åäö']))
