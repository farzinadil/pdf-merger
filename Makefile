.PHONY: install run test

# Install dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run the main merge script.
run:
	python merge.py

# Run the tests using pytest.
test:
	pytest --maxfail=1 --disable-warnings -q
