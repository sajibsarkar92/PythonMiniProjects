.PHONY: help run clean install test

help:
	@echo "Turtle Crossing Game - Available Commands"
	@echo "=========================================="
	@echo "make run      - Run the game"
	@echo "make clean    - Remove __pycache__ and .pyc files"
	@echo "make help     - Show this help message"

run:
	python main.py

clean:
	@echo "Cleaning up..."
	@for /d /r . %d in (__pycache__) do @if exist "%d" rmdir /s /q "%d"
	@del /s /q *.pyc 2>nul || true
	@echo "Cleanup complete!"

.DEFAULT_GOAL := help

