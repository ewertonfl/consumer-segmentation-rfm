# Makefile para automacao de comandos

PYTHON = python
PIP = pip

setup:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m src.pipeline

test:
	pytest tests/ -v

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__