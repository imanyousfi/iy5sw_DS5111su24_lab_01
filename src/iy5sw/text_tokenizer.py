"""
This module provides functions to clean text, tokenize text, and count words.
"""

import logging
import re
from collections import Counter

# configure the logging module:
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    """
    Converts string to all lowercase and removes punctuation.

    Parameters:
    - text (str): Given string

    Returns:
    - cleaned_text (str): string in all lowercase and no punctuations
    """
    assert isinstance(text, str), 'Input needs to be in string format'
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    logging.info('Text is being cleaned')

    assert isinstance(cleaned_text, str), 'Clean text needs to be in string format'
    assert cleaned_text is not None, 'Output is none'
    logging.info('Text is cleaned')

    return cleaned_text

def tokenize(text):
    """
    Converts string into a python list where each item is a word in the file.

    Parameters:
    - text (str): Given string

    Returns:
    - tokenized_text (list): list where each item is a word in a file
    """
    assert isinstance(text, str), 'input needs to be in string format'
    logging.info('Text is being tokenized')
    tokenized_text = text.split()

    assert isinstance(tokenized_text, list), 'Clean text needs to be in string format'
    assert tokenized_text is not None, 'Output is none'
    logging.info('Text is tokenized')

    return tokenized_text

def count_words(text):
    """
    Counts the frequency of each word in the given text.

    Parameters:
    - text (str): Given string

    Returns:
    - word_count (Counter): Counter object with word frequencies
    """
    tokenized_text = tokenize(text)
    word_count = Counter(tokenized_text)
    logging.info('Words are being counted')

    return word_count
