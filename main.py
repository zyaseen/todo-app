#!/usr/bin/env python3
"""
Main entry point for the Todo CLI application.

This file provides a direct way to run the todo application
using the command: uv run main.py

By default, it runs the interactive version.
"""

import sys
import os
# Add the project root directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from interactive_todo import main


if __name__ == "__main__":
    main()