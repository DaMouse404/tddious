# TDD shouldn't be TDDious
This is the codebase associated with my [pyData Warsaw talk about TDD](https://pydata.org/warsaw2019/schedule/presentation/20/tdd-shouldnt-be-tddious/).

## Notebook
To load the notebook, you can run:

```
make notebook
```

This will create the virtual environment and launch Jupyter.

## Tests
Similarly, to run the tests, you can run:

```
make test
```

Optionally you can filter it to a specific file or test:

```
make test FILTER=test/test_pipeline.py
```