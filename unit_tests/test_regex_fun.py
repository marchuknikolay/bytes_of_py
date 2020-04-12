from unittest import TestCase

from solutions.regex_fun import extract_course_times, get_all_hashtags_and_links, match_first_paragraph


class Test(TestCase):
    def test_extract_course_times_default_arg(self):
        expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
        self.assertEqual(expected, extract_course_times())

    def test_extract_course_times(self):
        course = ('00:40 Lesson introduction'
                  '01:33 Your 3 day overview'
                  '08:12 Learning datetime and date'
                  '06:07 Datetime timedelta usage'
                  '04:02 Concepts: what did we learn')
        expected = ['00:40', '01:33', '08:12', '06:07', '04:02']
        self.assertEqual(expected, extract_course_times(course))

    def test_get_all_hashtags_and_links_default_arg(self):
        expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
        self.assertEqual(expected, get_all_hashtags_and_links())

    def test_get_all_hashtags_and_links(self):
        tweet = ('PyBites My Reading List | 12 Rules for Life - #books '
                 'that expand the mind! '
                 'http://pbreadinglist.herokuapp.com/books/'
                 'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
                 ' #psychology #philosophy')
        expected = ['#books',
                    ('http://pbreadinglist.herokuapp.com/books/'
                     'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'),
                    '#psychology', '#philosophy']
        self.assertEqual(expected, get_all_hashtags_and_links(tweet))

    def test_match_first_paragraph_default_arg(self):
        expected = 'pybites != greedy'
        self.assertEqual(expected, match_first_paragraph())

    def test_match_first_paragraph(self):
        html = ('<p>Match only this paragraph.</p>'
                '<p>Not this one!</p><p>And this one neither.</p>')
        expected = 'Match only this paragraph.'
        self.assertEqual(expected, match_first_paragraph(html))
