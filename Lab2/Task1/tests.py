import unittest

from tools.statistics import (
    get_amount_of_sentences,
    get_amount_of_nondecl_sentences,
    get_avg_sentence_length,
    get_avg_word_length,
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


class TestCountNonDeclarative(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(get_amount_of_nondecl_sentences("  .. . . . .. !?? !?? ? !? ! ?! "), 0)
        self.assertEqual(get_amount_of_nondecl_sentences(""), 0)

    def test_one_non_declarative(self):
        self.assertEqual(get_amount_of_nondecl_sentences("Word...!??!!??!?!"), 1)
        self.assertEqual(get_amount_of_nondecl_sentences("A12..A12.!!!? B1500  ;;;"), 1)

    def test_many_non_declarative_many_signs(self):
        self.assertEqual(get_amount_of_nondecl_sentences("a...!?? ----!!?? a b!? c..!"), 3)

    def test_many_sentences_many_words(self):
        self.assertEqual(get_amount_of_nondecl_sentences("shibidibob, yes, yes! 2134 ! ; ... dob! dob! dob...",), 3)


class TestAverageSentenceLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(get_avg_sentence_length(""), 0)
        self.assertEqual(get_avg_sentence_length(
            "  .. . . . .. !?? !?? ? !? ! ?! "), 0)

    def test_one_char_long(self):
        self.assertEqual(get_avg_sentence_length("a...!??!!??!?!"), 1)
        self.assertEqual(get_avg_sentence_length(" 21321 ! =-=-/ B. 13 "), 1)

    def test_two_sentences_many_words(self):
        self.assertEqual(get_avg_sentence_length(
            """What determines the fate of humanity in this world?
            Some invisible being or law, like the Hand of the Lord hovering over the world?"""), 52.5)


class TestAverageWordLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(get_avg_word_length("  .. . .. !?? !? ? !? ?! "), 0)
        self.assertEqual(get_avg_word_length(""), 0)

    def test_one_letter(self):
        self.assertEqual(get_avg_word_length("A."), 1)

    def test_one_word_many_letters(self):
        self.assertEqual(get_avg_word_length(
            "WASSAPNIGAGTFOFMYCAR 0_0 IMNOTRACIST."), 11.0)

    def test_many_words_many_letters(self):
        self.assertEqual(get_avg_word_length("abba sus 124912 imp0ster."), 5)


if __name__ == "__main__":
  unittest.main()