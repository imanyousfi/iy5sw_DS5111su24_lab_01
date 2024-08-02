import os
import sys
import logging 
import re 
from collections import Counter
import pytest
# configure the logging module: 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from iy5sw.text_tokenizer import tokenize 

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


# Test with a given sample text:
def test_tokenize(sample_text): 
    # Given a string _text_ of the text with words
    # When we call the function tokenize with the text
    tokenized_text = tokenize(sample_text)
    # Then I should get a list of words in the text
    assert isinstance(tokenized_text, list), 'Output needs to be a list'


## Test with the intention to fail: 
@intentional_fail
def test_tokenize_fail(sample_text_list):
    # Given a list of words instead of string
    # When I call the function tokenize with the list of words
    tokenized_text = tokenize(sample_text)
    # I should get an assertion error
    assert tokenized_text == ['But', 'the', 'Raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'That', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour'], 'Test failed'
    
# write test for tokenize function using raven_text:
def test_tokenize_raven(raven_text):
    # Given the Raven text string 
    # When I call the tokenize function on the Raven file: 
    tokenized_raven_text = tokenize(raven_text)
    # Then I should get a list of words in the text
    assert isinstance(tokenized_raven_text, list), 'Output needs to be in list format'
   
# Test that parametrize a list of English files and test them independtly  
@pytest.mark.parametrize('file', all_text)
def test_clean_text_all_files(file, read_file):
    # Given a list of English files 
    # When I call the tokenize function on each file
    tokenized_text = tokenize(read_file(file))
    # Then I should get a list of words in the text
    assert isinstance(tokenized_text, list), 'Output needs to be in list format'

# Test all of the English files
def test_clean_text_combined(all_text_combined): 
# Given a list of English files
# When I call the function clean_text on each of the English files
    tokenized_all_text = tokenize(all_text_combined)
# Then I should get a cleaned text string with no punctuation and all lowercase
    assert isinstance(tokenized_all_text, list), 'Output needs to be in list format'  

# Test for Le Corbeau 
def test_clean_text_le_corbeu(le_corbeu):
    # Given the French text string 
    # When I call the clean_text function on the French text: 
    tokenized_le_corbeu = tokenize(le_corbeu)
    # Then I should get a cleaned French text string with no punctuation and all lowercase
    assert isinstance(tokenized_le_corbeu, list), 'Output needs to be in list format'
