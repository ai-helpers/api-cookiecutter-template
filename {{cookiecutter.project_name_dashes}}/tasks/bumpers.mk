bump-python-version: isset-PYTHON_VERSION ## Bump the python version installed.
	echo "$(PYTHON_VERSION)" > .python-version

bump-python-project: isset-PYTHON_VERSION ## Bump the python version of the project.
	sed -i.bak 's/^python = .*/python = "^$(PYTHON_VERSION)"/' pyproject.toml && rm pyproject.toml.bak

bump-package-project: isset-PACKAGE_VERSION ## Bump the package version of the project.
	sed -i.bak 's/^version = .*/version = "$(PACKAGE_VERSION)"/' pyproject.toml && rm pyproject.toml.bak
	sed -i.bak 's/^__version__ = .*/__version__ = "$(PACKAGE_VERSION)"/' src/{{cookiecutter.project_name_underscores}}/__init__.py && rm src/{{cookiecutter.project_name_underscores}}/__init__.py.bak

bump-package-sphinxdocs: isset-PACKAGE_VERSION ## Bump the package version of the documentation.
	sed -i.bak 's/^version = .*/version = "$(PACKAGE_VERSION)"/' docs/source/conf.py && rm docs/source/conf.py.bak

bump-python: bump-python-version bump-python-project ## Run all the python bumpers.

bump-package: bump-package-project bump-package-sphinxdocs ## Run all the package bumpers.