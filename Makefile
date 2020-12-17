brain-games:
		poetry run brain-games

build:
		poetry build ${arg}

install:
		poetry install

lint:
		poetry run flake8 brain_games

publish:
		poetry publish --dry-run

package-install:
		pip install --user dist/*.whl
