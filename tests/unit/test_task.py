"""
Unit tests for the Task class in the Todo CLI application.
"""
import pytest
from src.todo.task import Task
from src.todo.errors import InvalidTaskError


class TestTask:
    """
    Unit tests for the Task class.
    """
    
    def test_task_creation_with_valid_data(self):
        """
        Test creating a Task with valid data.
        """
        task = Task(id=1, title="Test task", description="Test description", completed=False)
        
        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False

    def test_task_creation_with_defaults(self):
        """
        Test creating a Task with default values.
        """
        task = Task(id=1, title="Test task")
        
        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == ""
        assert task.completed is False

    def test_task_creation_with_empty_title_raises_error(self):
        """
        Test that creating a Task with an empty title raises a ValueError.
        """
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="")

    def test_task_creation_with_whitespace_only_title_raises_error(self):
        """
        Test that creating a Task with a whitespace-only title raises a ValueError.
        """
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="   ")

    def test_task_creation_with_none_title_raises_error(self):
        """
        Test that creating a Task with a None title raises a ValueError.
        """
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title=None)