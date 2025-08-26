APP_NAME=folder-vision
IMAGE_NAME=folder-vision:latest

.PHONY: venv install run dev test test-cov build publish docker-build docker-run zip dist-zip binary clean

venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip

install: venv
	. .venv/bin/activate && pip install -r requirements.txt
	. .venv/bin/activate && pip install -e .[dev]

run:
	. .venv/bin/activate && uvicorn folder_vision.app:app --host 0.0.0.0 --port 8000 --reload

dev: run

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm -p 8000:8000 $(IMAGE_NAME)

zip:
	zip -r $(APP_NAME).zip folder_vision requirements.txt run.py README.md pyproject.toml Dockerfile Makefile .dockerignore

dist-zip:
	bash scripts/build_zip.sh

binary:
	. .venv/bin/activate || (echo "Run 'make install' first" && exit 1); \
	pip install pyinstaller && \
	pyinstaller -F -n $(APP_NAME) run.py

test:
	. .venv/bin/activate && pytest -q

test-cov:
	. .venv/bin/activate && pytest --cov=folder_vision --cov-report=term-missing

build:
	. .venv/bin/activate && python -m build

publish: build
	. .venv/bin/activate && pip install -q twine && twine upload dist/*

clean:
	rm -rf __pycache__ .venv build dist *.egg-info $(APP_NAME).zip folder_vision.egg-info

rebuild: clean build

install-global:
	pip install dist/$(APP_NAME)-*.whl --force-reinstall

test-install: build
	pip install dist/$(APP_NAME)-*.whl --force-reinstall
	folder-vision --version || python -m folder_vision --version
