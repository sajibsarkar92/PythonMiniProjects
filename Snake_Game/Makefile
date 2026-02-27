.PHONY: help install run clean test

help:
	@echo "Snake Game - Makefile Commands"
	@echo "=============================="
	@echo "make install   - Install project dependencies"
	@echo "make run       - Run the Snake Game"
	@echo "make clean     - Clean up cache files and temporary files"
	@echo "make help      - Show this help message"

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	python main.py

clean:
	@echo "Cleaning up cache files..."
	rmdir /s /q __pycache__ 2>nul || echo "No __pycache__ directory found"
	del /q *.pyc 2>nul || echo "No .pyc files found"
	@echo "Cleanup complete"

