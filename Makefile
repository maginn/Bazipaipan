.PHONY: help build install test clean dev-install lint format

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

build:  ## Build the package
	python3 -m build

install:  ## Install the package
	pip install .

dev-install:  ## Install the package in development mode
	pip install -e .

test:  ## Run tests
	python3 -m unittest discover tests/ -v

run:  ## Run the main application
	python3 main.py

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:  ## Run linting
	python3 -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

format:  ## Format code
	python3 -m black .

requirements:  ## Install development requirements
	pip install build pytest flake8 black

check:  ## Check if the package can be built
	python3 setup.py check