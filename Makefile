.PHONY: virtualenv, deps

ENV_DIR=.venv
PIP=${ENV_DIR}/bin/pip

install: clean virtualenv deps

clean:
	rm -rf .venv .reports .pytest_cache *.egg-info

.ONESHELL:
virtualenv:
	python3 -m venv ${ENV_DIR}
	. ${ENV_DIR}/bin/activate
	${PIP} install pip~=19.0.1 setuptools~=40.8.0 wheel~=0.32.3

deps:
	. ${ENV_DIR}/bin/activate && ${PIP} install -e .[dev]

.ONESHELL:
check:
	. ${ENV_DIR}/bin/activate
	flake8 rfc6266_parser.py || exit 1
	pytest ${PYTEST_ARGS}
