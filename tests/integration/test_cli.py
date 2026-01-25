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

    def test_add_command_with_priority_and_tags(self):
        """
        Test the add command with priority and tags.
        """
        cli = TodoCLI()

        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'add "Test task" --priority high --tags "work,urgent"'
            with patch('sys.argv', ['todo', 'add', 'Test task', '--priority', 'high', '--tags', 'work,urgent']):
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

    def test_list_command_with_filters(self):
        """
        Test the list command with filters applied.
        """
        cli = TodoCLI()

        # Add tasks with different priorities and tags
        cli.add_task("High priority task", "Description", "high", ["work"])
        cli.add_task("Low priority task", "Description", "low", ["home"])
        cli.add_task("Medium priority task", "Description", "medium", ["work"])

        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'list --priority high'
            with patch('sys.argv', ['todo', 'list', '--priority', 'high']):
                try:
                    cli.run()
                except SystemExit:
                    pass

        output = captured_output.getvalue()
        assert "High priority task" in output
        # Ensure other tasks are not shown
        assert "Low priority task" not in output
        assert "Medium priority task" not in output

    def test_list_command_with_search(self):
        """
        Test the list command with search functionality.
        """
        cli = TodoCLI()

        # Add tasks
        cli.add_task("Complete project", "Finish the specification document")
        cli.add_task("Buy groceries", "Milk and eggs")
        cli.add_task("Prepare presentation", "For the meeting")

        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'list --search "project"'
            with patch('sys.argv', ['todo', 'list', '--search', 'project']):
                try:
                    cli.run()
                except SystemExit:
                    pass

        output = captured_output.getvalue()
        assert "Complete project" in output
        # Ensure other tasks are not shown
        assert "Buy groceries" not in output
        assert "Prepare presentation" not in output

    def test_update_command_with_priority_and_tags(self):
        """
        Test the update command with priority and tags.
        """
        cli = TodoCLI()

        # Add a task first
        cli.add_task("Test task", "Test description")

        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'update 1 --priority high --tags "work,urgent"'
            with patch('sys.argv', ['todo', 'update', '1', '--priority', 'high', '--tags', 'work,urgent']):
                try:
                    cli.run()
                except SystemExit:
                    pass

        output = captured_output.getvalue()
        assert "Updated task with ID 1" in output

    def test_list_command_with_no_matching_filters(self):
        """
        Test the list command when no tasks match the filters.
        """
        cli = TodoCLI()

        # Add a task
        cli.add_task("Test task", "Test description", "low", ["home"])

        # Capture the output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Simulate command line arguments for 'list --priority high'
            with patch('sys.argv', ['todo', 'list', '--priority', 'high']):
                try:
                    cli.run()
                except SystemExit:
                    pass

        output = captured_output.getvalue()
        assert "No tasks match your search/filter criteria" in output