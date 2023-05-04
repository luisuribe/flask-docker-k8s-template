SHELL := /bin/bash
CWD := $(shell basename "$(shell pwd)")

docker-build:
	@echo $(CWD)
	docker build -t $(CWD) .

docker-run: docker-build
	docker run -p 5000:5000 -it $(CWD)

docker-unit-test: docker-build
	docker run -p 5000:5000 -it $(CWD) python3 -m unittest test_api.py

local:
	python3 api.py --debug run
