from .statistics_tools import *

def get_amount_of_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get amount of sentences """
    sentences = get_sentences(text, abbreviations)
    return len(sentences)

def get_amount_of_nondecl_sentences(text: str, abbreviations: str = ABBREVIATIONS):
    """ Get amount of non-declarative sentences in the text """
    sentences = get_sentences(text, abbreviations)
    return len([sentence for sentence in sentences if not is_declarative(sentence)])
