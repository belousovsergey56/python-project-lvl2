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
test:
	poetry run pytest --cov=differences/ --cov-report xml
remove:
	pip3 uninstall hexlet-code
reinstall:
	make remove
	make install
	make build
	make publish
	make package-install
diff:
	poetry run gendiff file_1.json file_2.json