from collections import Counter
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
    

def get_avg_word_length(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get average length of the word in the text in characters """

    sentences = get_sentences(text, abbreviations)
    clean_sentences = remove_not_words_and_symbols(sentences)
    words = get_words(clean_sentences)
    total_words = len(words)
    total_len = sum(len(word) for word in words)

    try:
        return total_len / total_words
    except ZeroDivisionError:
        return 0
    

def get_top_k_n_grams(text: str, abbreviations: str = ABBREVIATIONS, n: int = 4, k: int = 10):
    """ Get top-K repeated N-grams in the text """

    sentences = get_sentences(text, abbreviations)
    clean_sentences = remove_not_words_and_symbols(sentences)
    words = get_words(clean_sentences)

    ngrams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    ngram_freqs = Counter(ngrams)
    return ngram_freqs.most_common(k)