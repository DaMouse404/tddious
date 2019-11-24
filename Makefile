.PHONY: test

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r dev_requirements.txt

test: .venv
	PYTHONPATH=$(PWD) .venv/bin/pytest