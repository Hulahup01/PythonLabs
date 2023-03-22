import unittest

from tools.statistics import (
    get_amount_of_sentences,
)

class TestAmountOfSentences(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(get_amount_of_sentences(". . . ! wtf"), 0)
        self.assertEqual(get_amount_of_sentences(""), 0)

    def test_one_sentence(self):
        self.assertEqual(get_amount_of_sentences("sentence."), 1)
        self.assertEqual(get_amount_of_sentences(" 12 / .. / - A. 34 _;"), 1)

    def test_one_sentence_many_words(self):
        self.assertEqual(get_amount_of_sentences(
            "Something wr1te th3re 3 tms. blabla"), 1)

    def test_many_sentences_many_words(self):
        self.assertEqual(get_amount_of_sentences(
            "shibidibob, yes, yes! 2134 ! ; ... dob! dob! dob..."), 4)
        
if __name__ == "__main__":
  unittest.main()