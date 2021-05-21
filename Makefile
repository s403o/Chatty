setup:
	python3 -m venv ~/.chatty
	source ~/.chatty/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt