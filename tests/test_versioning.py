import os
import sys
import logging 
import re 
from collections import Counter
import pytest
# configure the logging module: 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from iy5sw.text_tokenizer import count_words

#Helper functions:

# sample text: 
@pytest.fixture
def sample_text():
    return "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."


# Test using the  skip decorator 
@pytest.mark.skip(reason="We are not ready to run the Japanese version yet")
def test_japanese_version():
    pass    

# Test for OS 
#def test_only_linux():
    #assert sys.platform == 'linux', 'This test is only for Linux'

# Test for Python Version 
def test_python_version():
    assert sys.version_info >= (3, 6), 'This test requires Python 3.6 or higher'
    
# Test uses bash/linux to get a results on a test string 
#def test_bash_wc(sample_text):
    # Given a string _text_ of the text with words
    # When we call the bash command wc with the text
    #result = os.popen(f'echo "{sample_text}" | wc').read()
    # Then we should get the same result as the count_words function
    #assert result == count_words(sample_text), 'Test failed'



