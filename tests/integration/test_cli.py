"""
Integration tests for the CLI functionality in the Todo CLI application.
"""
import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.todo.cli import TodoCLI


class TestCLI:
    """
    Integration tests for the CLI functionality.
    """
    
    def test_add_command_with_title_only(self):
        """
        Test the add command with only a title.
        """
        cli = TodoCLI()
        
        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'add "Test task"'
            with patch('sys.argv', ['todo', 'add', 'Test task']):
                try:
                    # Temporarily modify sys.argv for the parser
                    cli.run()
                except SystemExit:
                    # argparse calls sys.exit() after parsing, which is expected
                    pass
        
        output = captured_output.getvalue()
        assert "Added task 'Test task'" in output

    def test_add_command_with_title_and_description(self):
        """
        Test the add command with both title and description.
        """
        cli = TodoCLI()
        
        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'add "Test task" --desc "Test description"'
            with patch('sys.argv', ['todo', 'add', 'Test task', '--desc', 'Test description']):
                try:
                    cli.run()
                except SystemExit:
                    pass
        
        output = captured_output.getvalue()
        assert "Added task 'Test task'" in output

    def test_list_command_empty_list(self):
        """
        Test the list command when the list is empty.
        """
        cli = TodoCLI()
        
        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'list'
            with patch('sys.argv', ['todo', 'list']):
                try:
                    cli.run()
                except SystemExit:
                    pass
        
        output = captured_output.getvalue()
        assert "No tasks found" in output

    def test_list_command_with_tasks(self):
        """
        Test the list command when the list has tasks.
        """
        cli = TodoCLI()
        
        # First add a task
        cli.add_task("Test task", "Test description")
        
        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'list'
            with patch('sys.argv', ['todo', 'list']):
                try:
                    cli.run()
                except SystemExit:
                    pass
        
        output = captured_output.getvalue()
        assert "Test task" in output
        assert "Test description" in output