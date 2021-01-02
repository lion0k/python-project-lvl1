brain-games:
		python -m brain_games.scripts.brain_games

brain-calc:
		python -m brain_games.scripts.brain_calc

brain-even:
		python -m brain_games.scripts.brain_even

brain-gcd:
		python -m brain_games.scripts.brain_gcd

brain-progression:
		python -m brain_games.scripts.brain_progression

brain-prime:
		python -m brain_games.scripts.brain_prime

build:
		poetry build

install:
		poetry install

lint:
		poetry run flake8 brain_games

publish:
		poetry publish --dry-run

package-install:
		pip install --user dist/*.whl

git: gitadd gitcom gitpush

gitadd:
	git add -A .

gitcom:
	git commit -m "$(C)"

gitpush:
	git push

release:
	git tag v0.1.$(P)
	git push origin v0.1.$(P)
