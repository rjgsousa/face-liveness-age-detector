CWD = $(shell pwd)

PROJECT_NAME = flad
DOC_PROJECTS = docs
BIN_PROJECTS = $(PROJECTS)

documentation:
	for project in $(DOC_PROJECTS); do \
		cd $$project && $(MAKE) documentation && cd $(CWD) ; \
	done

clean_documentation:
	cd $(DOC_PROJECTS) && $(MAKE) clean && cd $(CWD)

clean: clean_documentation
	@rm -rfv build/ dist/ *.egg-info
	@find . -iname "*.pyc" | xargs --no-run-if-empty rm -rfv
	@rm -fv .coverage*
	@rm -rfv .pytest_cache test-results htmlcov
	@find . -iname "__pycache__" -type d | xargs --no-run-if-empty rm -rfv
	@rm -rfv .tox
	@pip uninstall -y $(PROJECT_NAME)

install:
	pip install poetry==1.8.2
	poetry install

dvc-update:
	@echo "Downloading required files... "
	dvc pull

run-experiment-standalone: install dvc-update
	@echo "######################### Processing video"
	python flad/main.py --video-file-path data/external/Faces\ from\ around\ the\ world.mp4
