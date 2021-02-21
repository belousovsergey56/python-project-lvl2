install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 differences
remove:
	pip3 uninstall hexlet-code
reinstall:
	make remove
	make install
	make build
	make publish
	make package-install