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
        assert task.priority is None
        assert task.tags == []
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
        assert task.priority is None
        assert task.tags == []
        assert len(todo_list.tasks) == 1
        assert todo_list.tasks[0] == task

    def test_add_task_with_priority_and_tags(self):
        """
        Test adding a task with priority and tags.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task", "Test description", "high", ["work", "urgent"])

        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False
        assert task.priority == "high"
        assert task.tags == ["work", "urgent"]
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
        assert retrieved_task.priority == added_task.priority
        assert retrieved_task.tags == added_task.tags

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

    def test_update_task_priority_only(self):
        """
        Test updating only the priority of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")

        success = todo_list.update_task(task.id, priority="high")

        assert success is True
        assert task.priority == "high"

    def test_update_task_tags_only(self):
        """
        Test updating only the tags of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Test task")

        success = todo_list.update_task(task.id, tags=["work", "urgent"])

        assert success is True
        assert task.tags == ["work", "urgent"]

    def test_update_task_all_fields(self):
        """
        Test updating all fields of a task.
        """
        todo_list = TodoList()
        task = todo_list.add_task("Original title", "Original description", "low", ["home"])

        success = todo_list.update_task(task.id, title="New title", description="New description",
                                        priority="high", tags=["work", "urgent"])

        assert success is True
        assert task.title == "New title"
        assert task.description == "New description"
        assert task.priority == "high"
        assert task.tags == ["work", "urgent"]

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

    def test_search_tasks_by_title(self):
        """
        Test searching tasks by title.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Buy groceries", "Milk and eggs")
        task2 = todo_list.add_task("Complete report", "Quarterly report")
        task3 = todo_list.add_task("Call mom", "Schedule appointment")

        results = todo_list.search_tasks("report")

        assert len(results) == 1
        assert task2 in results

    def test_search_tasks_by_description(self):
        """
        Test searching tasks by description.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Buy groceries", "Milk and eggs")
        task2 = todo_list.add_task("Complete report", "Quarterly report")
        task3 = todo_list.add_task("Call mom", "Schedule appointment")

        results = todo_list.search_tasks("appointment")

        assert len(results) == 1
        assert task3 in results

    def test_search_tasks_case_insensitive(self):
        """
        Test that searching is case insensitive.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Buy Groceries", "Milk and eggs")
        task2 = todo_list.add_task("Complete report", "QUARTERLY REPORT")

        results = todo_list.search_tasks("GROCERIES")

        assert len(results) == 1
        assert task1 in results

    def test_filter_tasks_by_status(self):
        """
        Test filtering tasks by completion status.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Incomplete task", "Description")
        task2 = todo_list.add_task("Complete task", "Description")
        todo_list.mark_task_complete(task2.id)

        incomplete_tasks = todo_list.filter_tasks(status="incomplete")
        complete_tasks = todo_list.filter_tasks(status="completed")

        assert len(incomplete_tasks) == 1
        assert task1 in incomplete_tasks
        assert len(complete_tasks) == 1
        assert task2 in complete_tasks

    def test_filter_tasks_by_priority(self):
        """
        Test filtering tasks by priority.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Low priority task", "Description", "low")
        task2 = todo_list.add_task("High priority task", "Description", "high")
        task3 = todo_list.add_task("Medium priority task", "Description", "medium")

        high_priority_tasks = todo_list.filter_tasks(priority="high")
        low_priority_tasks = todo_list.filter_tasks(priority="low")

        assert len(high_priority_tasks) == 1
        assert task2 in high_priority_tasks
        assert len(low_priority_tasks) == 1
        assert task1 in low_priority_tasks

    def test_filter_tasks_by_tag(self):
        """
        Test filtering tasks by tag.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Work task", "Description", tags=["work", "urgent"])
        task2 = todo_list.add_task("Home task", "Description", tags=["home", "chores"])
        task3 = todo_list.add_task("Personal task", "Description", tags=["personal"])

        work_tasks = todo_list.filter_tasks(tag="work")
        home_tasks = todo_list.filter_tasks(tag="home")

        assert len(work_tasks) == 1
        assert task1 in work_tasks
        assert len(home_tasks) == 1
        assert task2 in home_tasks

    def test_sort_tasks_by_priority(self):
        """
        Test sorting tasks by priority.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Low priority", "Description", "low")
        task2 = todo_list.add_task("High priority", "Description", "high")
        task3 = todo_list.add_task("Medium priority", "Description", "medium")

        sorted_tasks = todo_list.sort_tasks("priority")

        # High priority should come first, then medium, then low, then none
        assert sorted_tasks[0].priority == "high"
        assert sorted_tasks[1].priority == "medium"
        assert sorted_tasks[2].priority == "low"

    def test_sort_tasks_by_alpha(self):
        """
        Test sorting tasks alphabetically by title.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Zebra task", "Description")
        task2 = todo_list.add_task("Apple task", "Description")
        task3 = todo_list.add_task("Mango task", "Description")

        sorted_tasks = todo_list.sort_tasks("alpha")

        # Should be sorted alphabetically: Apple, Mango, Zebra
        assert sorted_tasks[0].title == "Apple task"
        assert sorted_tasks[1].title == "Mango task"
        assert sorted_tasks[2].title == "Zebra task"

    def test_sort_tasks_by_tags_count(self):
        """
        Test sorting tasks by number of tags.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Many tags", "Description", tags=["tag1", "tag2", "tag3"])
        task2 = todo_list.add_task("One tag", "Description", tags=["tag1"])
        task3 = todo_list.add_task("No tags", "Description", tags=[])

        sorted_tasks = todo_list.sort_tasks("tags")

        # Most tags first (descending by default): Many tags, One tag, No tags
        assert len(sorted_tasks[0].tags) >= len(sorted_tasks[1].tags)
        assert len(sorted_tasks[1].tags) >= len(sorted_tasks[2].tags)

    def test_combine_filters_search(self):
        """
        Test combining search and filters.
        """
        todo_list = TodoList()
        task1 = todo_list.add_task("Complete work report", "Description", "high", ["work", "urgent"])
        task2 = todo_list.add_task("Buy groceries", "Shopping list", "low", ["home"])
        task3 = todo_list.add_task("Review code", "Code review", "medium", ["work"])

        # Search for "work" and filter by high priority
        results = todo_list.combine_filters_search(search_keyword="work", priority="high")

        assert len(results) == 1
        assert task1 in results