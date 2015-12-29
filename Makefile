venv:
	virtualenv --python=python3 venv

clean:
	rm -rf venv

develop: venv
	. venv/bin/activate; \
	pip install -r requirements.txt

nopyc:
	find . -name '*.pyc' | xargs rm -f || true

install: develop


