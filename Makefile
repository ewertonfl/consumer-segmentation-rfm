setup:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python src/main.py
