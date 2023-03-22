from .statistics_tools import *

def get_amount_of_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get amount of sentences """
    sentences = get_sentences(text, abbreviations)
    return len(sentences)