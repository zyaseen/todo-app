"""
TodoList class for the Todo CLI application.

This module defines the TodoList class that manages a collection of Task objects
in memory with all required operations.
"""
from datetime import datetime, timedelta
from typing import List, Optional
from .task import Task


class TodoList:
    """
    Manages a collection of Task objects stored in memory.

    Attributes:
        tasks (List[Task]): Collection of Task objects stored in memory
        next_id (int): Next available ID to assign to a new task (starts at 1)
    """

    def __init__(self):
        """
        Initializes an empty TodoList with next_id starting at 1.
        """
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "", priority: Optional[str] = None,
                 tags: Optional[List[str]] = None, due_datetime: Optional[datetime] = None,
                 recurrence: Optional[dict] = None) -> Task:
        """
        Adds a new task with the given parameters.

        Args:
            title (str): The title of the task
            description (str): The optional description of the task
            priority (Optional[str]): The optional priority level (high, medium, low, or None)
            tags (Optional[List[str]]): The optional list of tags
            due_datetime (Optional[datetime]): The optional due date/time
            recurrence (Optional[dict]): The optional recurrence pattern

        Returns:
            Task: The newly created Task object
        """
        if tags is None:
            tags = []
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_datetime=due_datetime,
            recurrence=recurrence
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the list.

        Returns:
            List[Task]: All Task objects in the list
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Returns the task with the given ID, or None if not found.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    priority: Optional[str] = None, tags: Optional[List[str]] = None,
                    due_datetime: Optional[datetime] = None) -> bool:
        """
        Updates the title, description, priority, tags, and/or due date of an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): The new title (if provided)
            description (Optional[str]): The new description (if provided)
            priority (Optional[str]): The new priority (if provided)
            tags (Optional[List[str]]): The new list of tags (if provided)
            due_datetime (Optional[datetime]): The new due date/time (if provided)

        Returns:
            bool: True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            if tags is not None:
                task.tags = tags
            if due_datetime is not None:
                task.due_datetime = due_datetime
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes the task with the given ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Marks the task with the given ID as complete.

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            bool: True if the task was marked complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True

            # If the task is recurring, create the next instance
            if task.recurrence:
                self.process_completed_recurring_task(task_id)

            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Marks the task with the given ID as incomplete.

        Args:
            task_id (int): The ID of the task to mark incomplete

        Returns:
            bool: True if the task was marked incomplete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Searches tasks by keyword in title or description (case-insensitive).

        Args:
            keyword (str): The keyword to search for

        Returns:
            List[Task]: List of tasks that match the search criteria
        """
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if keyword_lower in task.title.lower() or keyword_lower in task.description.lower()
        ]

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, tag: Optional[str] = None) -> List[Task]:
        """
        Filters tasks by status, priority, or tag.

        Args:
            status (Optional[str]): Filter by completion status (all, incomplete, completed)
            priority (Optional[str]): Filter by priority (high, medium, low, none)
            tag (Optional[str]): Filter by tag presence

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = self.tasks[:]

        if status and status != "all":
            if status == "incomplete":
                filtered_tasks = [task for task in filtered_tasks if not task.completed]
            elif status == "completed":
                filtered_tasks = [task for task in filtered_tasks if task.completed]

        if priority:
            if priority == "none":
                filtered_tasks = [task for task in filtered_tasks if task.priority is None]
            else:
                filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

        if tag:
            filtered_tasks = [task for task in filtered_tasks if tag in task.tags]

        return filtered_tasks

    def sort_tasks(self, sort_by: str, reverse: bool = False) -> List[Task]:
        """
        Sorts tasks by the specified criteria.

        Args:
            sort_by (str): Sort by 'created', 'alpha', 'priority', or 'tags'
            reverse (bool): Whether to reverse the sort order

        Returns:
            List[Task]: List of tasks sorted by the specified criteria
        """
        if sort_by == "created":
            # Default order is by creation (ID), so no sorting needed
            return sorted(self.tasks, key=lambda x: x.id, reverse=reverse)
        elif sort_by == "alpha":
            return sorted(self.tasks, key=lambda x: x.title.lower(), reverse=reverse)
        elif sort_by == "priority":
            # Define priority order: high > medium > low > none
            priority_order = {"high": 3, "medium": 2, "low": 1, None: 0}
            return sorted(self.tasks, key=lambda x: priority_order[x.priority], reverse=not reverse)
        elif sort_by == "tags":
            # Sort by number of tags (most to least by default)
            return sorted(self.tasks, key=lambda x: len(x.tags), reverse=not reverse)
        else:
            # Default to created order if invalid sort_by
            return self.tasks[:]

    def get_overdue_tasks(self) -> List[Task]:
        """
        Returns all tasks that are overdue (due date is in the past and not completed).

        Returns:
            List[Task]: List of overdue tasks
        """
        now = datetime.now()
        return [
            task for task in self.tasks
            if task.due_datetime and not task.completed and task.due_datetime < now
        ]

    def get_due_soon_tasks(self, hours_ahead: int = 24) -> List[Task]:
        """
        Returns all tasks that are due soon (within the specified number of hours).

        Args:
            hours_ahead (int): Number of hours ahead to consider as "due soon" (default: 24)

        Returns:
            List[Task]: List of tasks due within the specified timeframe
        """
        now = datetime.now()
        future_time = now + timedelta(hours=hours_ahead)
        return [
            task for task in self.tasks
            if task.due_datetime and not task.completed and
            now < task.due_datetime <= future_time
        ]

    def get_due_today_tasks(self) -> List[Task]:
        """
        Returns all tasks that are due today (ignoring time component).

        Returns:
            List[Task]: List of tasks due today
        """
        now = datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        return [
            task for task in self.tasks
            if task.due_datetime and not task.completed and
            start_of_day <= task.due_datetime <= end_of_day
        ]

    def get_recurring_tasks(self) -> List[Task]:
        """
        Returns all recurring task templates.

        Returns:
            List[Task]: List of recurring task templates
        """
        return [task for task in self.tasks if task.recurrence is not None]

    def process_completed_recurring_task(self, task_id: int) -> Optional[Task]:
        """
        Creates the next instance of a recurring task when the current one is completed.

        Args:
            task_id (int): The ID of the completed recurring task

        Returns:
            Optional[Task]: The new task instance if created, None if task not found or not recurring
        """
        task = self.get_task_by_id(task_id)
        if not task or not task.recurrence:
            return None

        # Don't delete the original recurring template
        # Just mark the current instance as complete

        # Create a new instance based on the recurrence pattern
        if task.recurrence['type'] == 'daily':
            from datetime import timedelta
            new_due_date = task.due_datetime + timedelta(days=1) if task.due_datetime else None
        elif task.recurrence['type'] == 'weekly':
            from datetime import timedelta
            new_due_date = task.due_datetime + timedelta(weeks=1) if task.due_datetime else None
        elif task.recurrence['type'] == 'monthly':
            # For monthly, we'll add approximately one month
            # This is a simplified approach - a more robust solution would handle month boundaries
            if task.due_datetime:
                new_month = task.due_datetime.month + 1
                new_year = task.due_datetime.year
                if new_month > 12:
                    new_month = 1
                    new_year += 1
                new_due_date = task.due_datetime.replace(year=new_year, month=new_month)
            else:
                new_due_date = None
        elif task.recurrence['type'] == 'yearly':
            from datetime import timedelta
            new_due_date = task.due_datetime + timedelta(days=365) if task.due_datetime else None
        else:
            # Unsupported recurrence type
            return None

        # Check if there's an end condition
        end_date = task.recurrence.get('end_date')
        count = task.recurrence.get('count')

        # For now, we'll just create the next instance without checking end conditions
        # In a more complete implementation, we'd track how many instances were created

        # Create new task with updated due date
        new_task = self.add_task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            tags=task.tags,
            due_datetime=new_due_date,
            recurrence=task.recurrence
        )

        return new_task

    def combine_filters_search(self, search_keyword: Optional[str] = None, status: Optional[str] = None,
                              priority: Optional[str] = None, tag: Optional[str] = None,
                              sort_by: Optional[str] = None, reverse: bool = False) -> List[Task]:
        """
        Combines search, filters, and sorting operations.

        Args:
            search_keyword (Optional[str]): Keyword to search for
            status (Optional[str]): Filter by completion status
            priority (Optional[str]): Filter by priority
            tag (Optional[str]: Filter by tag presence
            sort_by (Optional[str]): Sort by criteria
            reverse (bool): Whether to reverse the sort order

        Returns:
            List[Task]: List of tasks that match all criteria and are sorted
        """
        # Start with all tasks
        result = self.tasks[:]

        # Apply search if provided
        if search_keyword:
            result = self.search_tasks(search_keyword)

        # Apply filters
        if status or priority or tag:
            # Create a temporary TodoList with filtered results to reuse filter_tasks method
            temp_todolist = TodoList()
            temp_todolist.tasks = result
            result = temp_todolist.filter_tasks(status, priority, tag)

        # Apply sorting if provided
        if sort_by:
            # Create a temporary TodoList with filtered results to reuse sort_tasks method
            temp_todolist = TodoList()
            temp_todolist.tasks = result
            result = temp_todolist.sort_tasks(sort_by, reverse)

        return result