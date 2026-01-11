"""
Unit tests for the TodoList class in the Todo CLI application.
"""
import pytest
from src.todo.todo_list import TodoList
from src.todo.task import Task


class TestTodoList:
    """
    Unit tests for the TodoList class.
    """
    
    def test_add_task_with_title_only(self):
        """
        Test adding a task with only a title.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")
        
        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == ""
        assert task.completed is False
        assert len(todo_list.tasks) == 1
        assert todo_list.tasks[0] == task

    def test_add_task_with_title_and_description(self):
        """
        Test adding a task with both title and description.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task", "Test description")
        
        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False
        assert len(todo_list.tasks) == 1
        assert todo_list.tasks[0] == task

    def test_add_multiple_tasks_increments_id(self):
        """
        Test that adding multiple tasks increments the ID correctly.
        """
        todo_list = TodoList()
        
        task1 = todo_list.add_task("First task")
        task2 = todo_list.add_task("Second task")
        task3 = todo_list.add_task("Third task")
        
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert len(todo_list.tasks) == 3

    def test_get_all_tasks(self):
        """
        Test getting all tasks from the list.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("First task")
        task2 = todo_list.add_task("Second task")
        
        all_tasks = todo_list.get_all_tasks()
        
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_get_task_by_id_found(self):
        """
        Test getting a task by ID when it exists.
        """
        todo_list = TodoList()
        added_task = todo_list.add_task("Test task")
        
        retrieved_task = todo_list.get_task_by_id(added_task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title
        assert retrieved_task.description == added_task.description
        assert retrieved_task.completed == added_task.completed

    def test_get_task_by_id_not_found(self):
        """
        Test getting a task by ID when it doesn't exist.
        """
        todo_list = TodoList()
        todo_list.add_task("Test task")
        
        retrieved_task = todo_list.get_task_by_id(999)
        
        assert retrieved_task is None

    def test_update_task_title_only(self):
        """
        Test updating only the title of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Original title", "Original description")
        
        success = todo_list.update_task(task.id, title="New title")
        
        assert success is True
        assert task.title == "New title"
        assert task.description == "Original description"

    def test_update_task_description_only(self):
        """
        Test updating only the description of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Original title", "Original description")
        
        success = todo_list.update_task(task.id, description="New description")
        
        assert success is True
        assert task.title == "Original title"
        assert task.description == "New description"

    def test_update_task_both_fields(self):
        """
        Test updating both title and description of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Original title", "Original description")
        
        success = todo_list.update_task(task.id, title="New title", description="New description")
        
        assert success is True
        assert task.title == "New title"
        assert task.description == "New description"

    def test_update_task_not_found(self):
        """
        Test updating a task that doesn't exist.
        """
        todo_list = TodoList()
        
        success = todo_list.update_task(999, title="New title")
        
        assert success is False

    def test_delete_task_exists(self):
        """
        Test deleting a task that exists.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")
        
        success = todo_list.delete_task(task.id)
        
        assert success is True
        assert len(todo_list.tasks) == 0

    def test_delete_task_not_found(self):
        """
        Test deleting a task that doesn't exist.
        """
        todo_list = TodoList()
        todo_list.add_task("Test task")
        
        success = todo_list.delete_task(999)
        
        assert success is False
        assert len(todo_list.tasks) == 1

    def test_mark_task_complete(self):
        """
        Test marking a task as complete.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")
        assert task.completed is False
        
        success = todo_list.mark_task_complete(task.id)
        
        assert success is True
        assert task.completed is True

    def test_mark_task_incomplete(self):
        """
        Test marking a task as incomplete.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")
        # First mark as complete
        todo_list.mark_task_complete(task.id)
        assert task.completed is True
        
        success = todo_list.mark_task_incomplete(task.id)
        
        assert success is True
        assert task.completed is False

    def test_mark_task_complete_not_found(self):
        """
        Test marking a task as complete when it doesn't exist.
        """
        todo_list = TodoList()
        
        success = todo_list.mark_task_complete(999)
        
        assert success is False

    def test_mark_task_incomplete_not_found(self):
        """
        Test marking a task as incomplete when it doesn't exist.
        """
        todo_list = TodoList()
        
        success = todo_list.mark_task_incomplete(999)
        
        assert success is False