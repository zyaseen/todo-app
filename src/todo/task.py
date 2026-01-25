"""
Task dataclass for the Todo CLI application.

This module defines the Task dataclass with id, title, description, completed, priority, tags, due_datetime, and recurrence fields,
along with validation for required fields.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Any


@dataclass
class Task:
    """
    Represents a single todo item.

    Attributes:
        id (int): Unique sequential identifier assigned when task is created
        title (str): Required title of the task (non-empty string validation required)
        description (str): Optional description of the task (can be empty)
        completed (bool): Boolean indicating completion status (default: False)
        priority (Optional[str]): Priority level of the task: "high", "medium", "low", or None (default: None)
        tags (List[str]): List of tags associated with the task (default: empty list)
        due_datetime (Optional[datetime]): Optional due date/time for the task (default: None)
        recurrence (Optional[Dict[str, Any]]): Optional recurrence pattern information (default: None)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Optional[str] = None
    tags: List[str] = None
    due_datetime: Optional[datetime] = None
    recurrence: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        """
        Validates the Task instance after initialization.

        Ensures that the title is not empty and priority is valid.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        if self.priority is not None and self.priority not in ["high", "medium", "low"]:
            raise ValueError(f"Invalid priority value: {self.priority}. Must be one of: high, medium, low, or None")

        if self.tags is None:
            self.tags = []

        if self.recurrence is not None:
            self.validate_recurrence()

    def validate_recurrence(self):
        """
        Validates the recurrence pattern if present.

        Ensures that the recurrence dictionary has the required structure.
        """
        if not isinstance(self.recurrence, dict):
            raise ValueError("Recurrence must be a dictionary")

        if "type" not in self.recurrence:
            raise ValueError("Recurrence must have a 'type' field")

        recurrence_type = self.recurrence["type"]
        if recurrence_type not in ["daily", "weekly", "monthly", "yearly"]:
            raise ValueError(f"Invalid recurrence type: {recurrence_type}. Must be one of: daily, weekly, monthly, yearly")

        # Validate weekly recurrence has a weekday
        if recurrence_type == "weekly":
            if "weekday" not in self.recurrence:
                raise ValueError("Weekly recurrence must specify a 'weekday'")
            weekday = self.recurrence["weekday"]
            valid_weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            if weekday not in valid_weekdays:
                raise ValueError(f"Invalid weekday: {weekday}. Must be one of: {valid_weekdays}")

        # Validate monthly recurrence has a day
        if recurrence_type == "monthly":
            if "day" not in self.recurrence:
                raise ValueError("Monthly recurrence must specify a 'day'")
            try:
                day = int(self.recurrence["day"])
                if day < 1 or day > 31:
                    raise ValueError(f"Invalid day for monthly recurrence: {day}. Must be between 1 and 31")
            except ValueError as e:
                if "invalid literal" in str(e):
                    raise ValueError(f"Invalid day for monthly recurrence: {self.recurrence['day']}. Must be a number between 1 and 31")
                else:
                    raise e