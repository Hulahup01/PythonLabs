from .statistics_tools import *


def get_amount_of_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get amount of sentences """
    sentences = get_sentences(text, abbreviations)
    return len(sentences)


def get_amount_of_nondecl_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get amount of non-declarative sentences in the text """
    sentences = get_sentences(text, abbreviations)
    return len([sentence for sentence in sentences if not is_declarative(sentence)])


def get_avg_sentence_length(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get average length of the sentence in characters """

    sentences = get_sentences(text, abbreviations)
    clean_sentences = remove_not_words_and_symbols(sentences)
    total_words = sum(len(sent.replace(" ", "")) for sent in clean_sentences)

    try:
        return total_words / len(sentences)
    except ZeroDivisionError:
        return 0