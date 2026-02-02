```makefile
PY=python3

.PHONY: install run debug clean lint lint-strict

install:
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install flake8 mypy

run:
	$(PY) a_maze_ing.py config_default.txt

debug:
	$(PY) -m pdb a_maze_ing.py config_default.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + || true

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
