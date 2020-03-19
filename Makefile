init:
	pip install -r requirements.txt
test:
	python -m unittest -v tests.hello_world
	python -m unittest -v tests.test_matrices
.PHONY: init test