init:
	git init
	pre-commit install
	pre-commit autoupdate
	poetry update
	poetry install
	git add .
	git commit -m ":tada: Initial commit."

lint:
	pre-commit run --all-files

test:
	poetry install
	poetry run pytest

test_ipdb:
	poetry install
	poetry run pytest \
		--pdbcls=IPython.terminal.debugger:TerminalPdb \
		--pdb

freeze:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

freeze_dev:
	poetry export -f requirements.txt --dev --output requirements.txt --without-hashes

update:
	poetry update
	pre-commit autoupdate
{%- if cookiecutter.use_docker == 'y' %}

docker:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build -t {{cookiecutter.project_slug}} .
{%- endif %}
