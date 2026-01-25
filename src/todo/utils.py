"""
Utility functions for the Todo CLI application.

This module provides helper functions for date parsing and other utilities.
"""
from datetime import datetime, timedelta
from typing import Union


def parse_date_string(date_string: str) -> datetime:
    """
    Parses a date string into a datetime object.
    
    Supports various formats:
    - YYYY-MM-DD
    - YYYY-MM-DD HH:MM
    - Relative formats like: "tomorrow", "today", "next friday", "in 2 days"
    
    Args:
        date_string (str): Date string in one of the supported formats
        
    Returns:
        datetime: Parsed datetime object
        
    Raises:
        ValueError: If the date string format is not recognized
    """
    date_string = date_string.strip().lower()
    
    # Handle relative dates
    if date_string == "today":
        return datetime.combine(datetime.today().date(), datetime.min.time())
    elif date_string == "tomorrow":
        tomorrow = datetime.today().date() + timedelta(days=1)
        return datetime.combine(tomorrow, datetime.min.time())
    elif date_string.startswith("in ") and date_string.endswith(" days"):
        try:
            num_days = int(date_string[3:-5])  # Extract number from "in X days"
            future_date = datetime.today().date() + timedelta(days=num_days)
            return datetime.combine(future_date, datetime.min.time())
        except ValueError:
            pass  # Will continue to try other formats
    
    # Handle "next <weekday>"
    weekdays = {
        "monday": 0, "mon": 0,
        "tuesday": 1, "tue": 1,
        "wednesday": 2, "wed": 2,
        "thursday": 3, "thu": 3,
        "friday": 4, "fri": 4,
        "saturday": 5, "sat": 5,
        "sunday": 6, "sun": 6
    }
    
    if date_string.startswith("next "):
        weekday_name = date_string[5:]  # Get the weekday part
        if weekday_name in weekdays:
            today = datetime.today()
            target_weekday = weekdays[weekday_name]
            days_ahead = target_weekday - today.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
            future_date = today.date() + timedelta(days=days_ahead)
            return datetime.combine(future_date, datetime.min.time())
    
    # Handle time specifications like "tomorrow 3pm", "next friday 9am"
    if "tomorrow" in date_string:
        time_part = date_string.replace("tomorrow", "").strip()
        base_date = datetime.today().date() + timedelta(days=1)
        return _parse_time_on_date(time_part, base_date)
    elif "today" in date_string:
        time_part = date_string.replace("today", "").strip()
        base_date = datetime.today().date()
        return _parse_time_on_date(time_part, base_date)
    
    # Handle standard formats: YYYY-MM-DD or YYYY-MM-DD HH:MM
    try:
        # Try parsing as YYYY-MM-DD first
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        try:
            # Try parsing as YYYY-MM-DD HH:MM
            return datetime.strptime(date_string, "%Y-%m-%d %H:%M")
        except ValueError:
            # Try parsing as YYYY-MM-DD HH:MM:SS
            try:
                return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass
    
    raise ValueError(f"Unable to parse date string: {date_string}")


def _parse_time_on_date(time_part: str, date_obj: datetime.date) -> datetime:
    """
    Helper function to parse time specifications on a given date.

    Args:
        time_part (str): Time part of the string (e.g., "3pm", "9am", "15:00")
        date_obj (datetime.date): Date to apply the time to

    Returns:
        datetime: Combined datetime object
    """
    time_part = time_part.strip()

    if not time_part:
        # If no time specified, default to 00:00 (midnight)
        return datetime.combine(date_obj, datetime.min.time())

    # Handle "Xam" or "Xpm" formats
    if time_part.endswith("am") or time_part.endswith("pm"):
        hour_str = time_part[:-2].strip()
        is_pm = time_part[-2:] == "pm"

        try:
            hour = int(hour_str)
            if hour == 12:
                # Special case for 12-hour format: 12am is 00:00, 12pm is 12:00
                if not is_pm:  # 12am
                    hour = 0
            elif is_pm and hour < 12:  # PM hours except 12pm
                hour += 12
            elif not is_pm and hour == 12:  # 12am
                hour = 0

            return datetime.combine(date_obj, datetime.min.time().replace(hour=hour))
        except ValueError:
            pass

    # Handle HH:MM format
    try:
        time_obj = datetime.strptime(time_part, "%H:%M").time()
        return datetime.combine(date_obj, time_obj)
    except ValueError:
        pass

    # Handle HH:MM:SS format
    try:
        time_obj = datetime.strptime(time_part, "%H:%M:%S").time()
        return datetime.combine(date_obj, time_obj)
    except ValueError:
        pass

    # Handle just hour format (e.g., "3" meaning 3:00)
    try:
        hour = int(time_part)
        if 0 <= hour <= 23:
            return datetime.combine(date_obj, datetime.min.time().replace(hour=hour))
    except ValueError:
        pass

    raise ValueError(f"Unable to parse time: {time_part}")