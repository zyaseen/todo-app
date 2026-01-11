"""
TodoList class for the Todo CLI application.

This module defines the TodoList class that manages a collection of Task objects
in memory with all required operations.
"""
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

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Adds a new task with the given title and optional description.
        
        Args:
            title (str): The title of the task
            description (str): The optional description of the task
            
        Returns:
            Task: The newly created Task object
        """
        task = Task(id=self.next_id, title=title, description=description)
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates the title and/or description of an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): The new title (if provided)
            description (Optional[str]): The new description (if provided)
            
        Returns:
            bool: True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
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