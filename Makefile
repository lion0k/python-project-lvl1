brain-games:
		poetry run brain-games

brain-calc:
		poetry run brain-calc

brain-even:
		poetry run brain-even

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime

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
