"""
Task dataclass for the Todo CLI application.

This module defines the Task dataclass with id, title, description, and completed fields,
along with validation for required fields.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item.
    
    Attributes:
        id (int): Unique sequential identifier assigned when task is created
        title (str): Required title of the task (non-empty string validation required)
        description (str): Optional description of the task (can be empty)
        completed (bool): Boolean indicating completion status (default: False)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """
        Validates the Task instance after initialization.
        
        Ensures that the title is not empty.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")