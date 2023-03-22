import re
from .text_constants import ABBREVIATIONS


def get_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get list of sentences in the text """

    for abbr in abbreviations.split(' '):
        pattern = re.compile(re.escape(" " + abbr + " "), re.IGNORECASE)
        text = pattern.sub(abbr.replace('.', ''), text)
    return remove_not_sentences(re.split('(?<=[.!?])\s+', text))


def remove_not_sentences(sentences: list):
    """ Romoving offers that are not offers from the list """

    new_sentences = [sent for sent in sentences if re.search(r'[a-zA-Z]', sent)]

    if len(new_sentences) != 0:
        if new_sentences[-1][-1] not in ('.', '?', '!'):
            new_sentences.pop()
    return new_sentences


def is_declarative(sentence: str):
    """ Checking checking for a declarative sentences"""
    return sentence.endswith('.') or sentence.endswith('...')


def remove_not_words_and_symbols(sentences: list):
    """ Removing from sentences not words and symbols"""
    new_sentences = []
    for sent in sentences:
        new_sentences.append(re.sub(r'\b\d+\b|[^a-zA-Z0-9 ]', '', sent))
    return new_sentences


def get_words(sentences: list):
    """ Get list of words from senteces """
    words = []
    for sent in sentences:
        words += sent.split()
    return words

