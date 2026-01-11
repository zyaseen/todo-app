"""
Error handling base classes for the Todo CLI application.
"""


class TodoError(Exception):
    """
    Base exception class for todo-related errors.
    """
    pass


class TaskNotFoundError(TodoError):
    """
    Raised when a task with a specific ID is not found.
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found")


class InvalidTaskError(TodoError):
    """
    Raised when a task is invalid (e.g., empty title).
    """
    def __init__(self, message: str):
        super().__init__(message)