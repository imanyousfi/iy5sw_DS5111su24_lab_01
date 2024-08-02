import os
import sys
import logging 
import re 
from collections import Counter
import pytest
# configure the logging module: 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from text_tokenizer import count_words

#Helper functions:

# sample text: 
@pytest.fixture
def sample_text():
    return "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

# sample text in list type:
@pytest.fixture
def sample_text_list():
    return ["But", "the", "Raven,", "sitting", "lonely", "on", "the", "placid", "bust,", "spoke", "only", "That", "one", "word,", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour."]

# create a decorator that prints that the test function fails on purpose
def intentional_fail(func):
    func = pytest.mark.xfail(func)
    def wrapper(*args, **kwargs):
        print(f'Test {func.__name__} is failing on purpose')
        return func(*args, **kwargs)
    return wrapper

# Raven file: 
@pytest.fixture
def raven_text():
    file_path = os.path.join('book_dict', 'pg17192.txt')
    with open(file_path, 'r') as file: 
        raven_text = file.read()
    return raven_text

# All English files: 
all_text = ['book_dict/pg17192.txt', 
            'book_dict/pg14082.txt', 
            'book_dict/pg10031.txt', 
            'book_dict/pg1063.txt', 
            'book_dict/pg932.txt']

# Reader for all English files:
@pytest.fixture
def read_file():
    def _read_file(file_path):
        with open(file_path, 'r') as file: 
            return file.read()
    return _read_file

# Combined text:
@pytest.fixture
def all_text_combined():
    all_text_combined = ''
    for file in all_text:
        with open(file, 'r') as f:
            all_text_combined += f.read()
    return all_text_combined

pytest.fixture
def le_corbeu():
    return "Mais le Corbeau, perché solitairement sur ce buste placide, parlace seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ontpris leur vol--demain il me laissera comme mes Espérances déjà ontpris leur vol Alors l'oiseau dit"


# Test a given a sample text
def test_count_words(sample_text):
    # Given a string _text_ of the text with words
    # When we call the function count_words with the text
    word_count = count_words(sample_text)
    # Then we should get a dictionary with words as keys and their count as values
    assert isinstance(word_count, Counter), 'Output needs to be a Counter object'   


# Test with the intention to fail: 
@intentional_fail
def test_count_words_fail(sample_text_list):
    # Given a list of words instead of string
    # When I call the function count_words with the list of words
    word_count = count_words(sample_text_list)
    # I should get an assertion error
    assert word_count == Counter({'But': 1, 'the': 2, 'Raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1, 'spoke': 1, 'only': 1, 'That': 1, 'one': 2, 'word': 2, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'he': 1, 'did': 1, 'outpour': 1}), 'Test failed'
    
# write test for count word function using raven_text:
def test_count_words_raven(raven_text_text):
    # Given the Raven text string 
    # When I call the count_words function on the Raven file: 
    word_count_raven = count_words(raven_text)
    # Then I should get a dictionary with words as keys and their count as values
    assert isinstance(word_count_raven, Counter), 'Output needs to be in Counter format'
    
# Test that parametrize a list of English files and test them independtly  
@pytest.mark.parametrize('file', all_text)
def test_count_words_all_files(file, read_file):
    # Given a list of English files 
    # When I call the count_words function on each file
    word_count = count_words(read_file(file))
    # Then I should get a dictionary with words as keys and their count as values
    assert isinstance(word_count, Counter), 'Output needs to be in Counter format'

# Test all of the English files
def test_count_words_combined(all_text_combined):
    # Given a list of English files
    # When I call the function count_words on each of the English files
    word_count = count_words(all_text_combined)
    # Then I should get a dictionary with words as keys and their count as values
    assert isinstance(word_count, Counter), 'Output needs to be in Counter format'


# Test for Le Corbeau 
def test_count_words_le_corbeu(le_corbeu):
    # Given the French text string 
    # When I call the count_words function on the French text: 
    word_count = count_words(le_corbeu)
    # Then I should get a dictionary with words as keys and their count as values
    assert isinstance(word_count, Counter), 'Output needs to be in Counter format'




