from .text_constants import ABBREVIATIONS
from .statistics_tools import (
    get_sentences,
    is_declarative,
    remove_not_words_and_symbols,
    get_words,
)


def get_statistics(text: str, abbr: str = ABBREVIATIONS):
    """ Get all statistics of the text """

    amount_of_sentences = get_amount_of_sentences(text, abbr)
    amount_of_non_declarative_sentences = get_amount_of_nondecl_sentences(text, abbr)
    avg_sentence_length = get_avg_sentence_length(text, abbr)
    avg_words_length = get_avg_word_length(text, abbr)
    top_k_n_grams = get_top_k_n_grams(text, abbr)

    return {
        'num_sentences': amount_of_sentences,
        'num_non_declarative': amount_of_non_declarative_sentences,
        'avg_sentence_length': avg_sentence_length,
        'average_word_length': avg_words_length,
        'top_k_n_grams': top_k_n_grams
    }


def get_amount_of_sentences(text: str, abbr: str = ABBREVIATIONS):
    """ Get amount of sentences """

    sentences = get_sentences(text, abbr)
    return len(sentences)


def get_amount_of_nondecl_sentences(text: str, abbr: str = ABBREVIATIONS):
    """ Get amount of non-declarative sentences in the text """

    sentences = get_sentences(text, abbr)
    return len([sentence
                for sentence in sentences
                if not is_declarative(sentence)])


def get_avg_sentence_length(text: str, abbr: str = ABBREVIATIONS):
    """ Get average length of the sentence in characters """

    sentences = get_sentences(text, abbr)
    clean_sentences = remove_not_words_and_symbols(sentences)
    total_words = sum(len(sent.replace(" ", "")) for sent in clean_sentences)

    try:
        return total_words / len(sentences)
    except ZeroDivisionError:
        return 0


def get_avg_word_length(text: str, abbr: str = ABBREVIATIONS):
    """ Get average length of the word in the text in characters """

    sentences = get_sentences(text, abbr)
    clean_sentences = remove_not_words_and_symbols(sentences)
    words = get_words(clean_sentences)
    total_words = len(words)
    total_len = sum(len(word) for word in words)

    try:
        return total_len / total_words
    except ZeroDivisionError:
        return 0


def get_top_k_n_grams(text: str, abbr: str = ABBREVIATIONS, n: int = 4, k: int = 10):
    """ Get top-K repeated N-grams in the text """

    sentences = get_sentences(text, abbr)
    clean_sentences = remove_not_words_and_symbols(sentences)
    words = get_words(clean_sentences)
    ngram_freqs = {}
    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i + n])
        ngram_freqs[ngram] = ngram_freqs.get(ngram, 0) + 1
    sorted_ngram_freqs = sorted(ngram_freqs.items(), key=lambda x: x[1], reverse=True)
    return sorted_ngram_freqs[:k]
