brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime

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
