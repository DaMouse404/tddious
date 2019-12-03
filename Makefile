.PHONY: test notebook

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r dev_requirements.txt
	.venv/bin/pip install -r requirements.txt

notebook:
	.venv/bin/jupyter notebook notebook/predict-result-for-pokemon-s-battle.ipynb

test: .venv
	PYTHONPATH=$(PWD) .venv/bin/pytest --durations=0 $(FILTER)