

default: 
	cat Makefile 

get_texts: 
	bash get_the_books.sh 

raven_line_count: 
	@echo "Raven Line Count:"
	 wc -l book_dict/pg17192.txt

raven_word_count: 
	@echo "Raven Word Count:"
	wc -w book_dict/pg17192.txt 

raven_counts: 
	@echo "Occurrences of 'raven' (lowercase):" 
	grep -o  'raven' book_dict/pg17192.txt | wc -l 

	@echo "Occurrences of 'Raven' (title case):"
	grep -o  'Raven'  book_dict/pg17192.txt | wc -l

	@echo "Occurrences of 'raven' (ignore case):"
	grep -o -i 'raven' book_dict/pg17192.txt | wc -l

total_lines: 
	@echo "Total Lines in All Files:" 
	cat book_dict/*.txt | wc -l 

total_words: 
	@echo "Total Words in All Files:"
	cat book_dict/*.txt | wc -w 

create_env: 
	python3 -m venv env
	pip install --upgrade pip 
	pip install pip 
	pip install -r requirements.txt

test:
	pip install -e .; . env/bin/activate; pytest -vvx tests/

lint: 
	. env/bin/activate; pylint src/iy5sw/text_tokenizer.py
