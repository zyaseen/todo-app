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
        task = Task(id=1, title="Test task", description="Test description", completed=False, priority="high", tags=["work", "urgent"])

        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False
        assert task.priority == "high"
        assert task.tags == ["work", "urgent"]

    def test_task_creation_with_defaults(self):
        """
        Test creating a Task with default values.
        """
        task = Task(id=1, title="Test task")

        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == ""
        assert task.completed is False
        assert task.priority is None
        assert task.tags == []

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

    def test_task_creation_with_invalid_priority_raises_error(self):
        """
        Test that creating a Task with an invalid priority raises a ValueError.
        """
        with pytest.raises(ValueError, match="Invalid priority value: invalid. Must be one of: high, medium, low, or None"):
            Task(id=1, title="Test task", priority="invalid")

    def test_task_creation_with_valid_priorities(self):
        """
        Test creating a Task with valid priority values.
        """
        for priority in ["high", "medium", "low", None]:
            task = Task(id=1, title="Test task", priority=priority)
            assert task.priority == priority

    def test_task_initializes_empty_tags_list(self):
        """
        Test that creating a Task with no tags initializes an empty tags list.
        """
        task = Task(id=1, title="Test task")
        assert task.tags == []