from unittest import TestCase

from solutions.sum_n_numbers import sum_numbers


class Test(TestCase):
    def test_sum_numbers_default_args(self):
        self.assertEqual(5050, sum_numbers())

    def test_sum_numbers_empty_list(self):
        self.assertEqual(0, sum_numbers([]))

    def test_sum_numbers(self):
        self.assertEqual(6, sum_numbers([1, 2, 3]))
