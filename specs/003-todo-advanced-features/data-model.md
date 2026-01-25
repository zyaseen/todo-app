# Data Model: Todo Advanced Features

## Extended Task Entity

### Fields
- **id**: `int` - Unique sequential identifier assigned when task is created
- **title**: `str` - Required title of the task (non-empty string validation required)
- **description**: `str` - Optional description of the task (can be empty)
- **completed**: `bool` - Boolean indicating completion status (default: False)
- **priority**: `Optional[str]` - Priority level: "high", "medium", "low", or None (default: None)
- **tags**: `list[str]` - List of tags associated with the task (default: empty list)
- **due_datetime**: `Optional[datetime.datetime]` - Optional due date/time for the task (default: None)
- **recurrence**: `Optional[dict]` - Recurrence pattern information (default: None)

### Validation Rules
- `title` must be a non-empty string (length > 0)
- `id` must be unique within the application session
- `id` must be a positive integer (≥ 1)
- `priority` must be one of: "high", "medium", "low", or None
- `due_datetime` must be a valid datetime or None
- `recurrence` must be a dictionary with required structure if present

### Recurrence Pattern Structure
When `recurrence` is not None, it must contain:
- **type**: `str` - One of "daily", "weekly", "monthly", "yearly"
- **interval**: `int` - Interval multiplier (e.g., every 2 weeks would have type="weekly", interval=2)
- **end_condition**: `Optional[dict]` - Optional end conditions with either:
  - **end_date**: `datetime.datetime` - Stop creating instances after this date
  - **occurrences**: `int` - Stop after creating this many total instances

### State Transitions
- `completed` state can transition from `False` to `True` (incomplete → complete)
- `completed` state can transition from `True` to `False` (complete → incomplete)
- `due_datetime` can be set/unset during updates
- When a recurring task is completed, a new instance is created according to the recurrence pattern

## Enhanced TodoList Entity

### Fields
- **tasks**: `List[Task]` - Collection of Task objects stored in memory
- **next_id**: `int` - Next available ID to assign to a new task (starts at 1)

### Validation Rules
- No two tasks can have the same ID
- Task IDs must be sequential and positive integers
- When a recurring task is completed, the original remains and a new instance is created

### Operations
- `add_task(title: str, description: str = "", priority: Optional[str] = None, tags: list[str] = [], due_datetime: Optional[datetime] = None, recurrence: Optional[dict] = None)` → `Task`
- `get_all_tasks()` → `List[Task]`
- `get_task_by_id(task_id: int)` → `Optional[Task]`
- `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, due_datetime: Optional[datetime] = None)` → `bool`
- `delete_task(task_id: int)` → `bool`
- `mark_task_complete(task_id: int)` → `bool`
- `mark_task_incomplete(task_id: int)` → `bool`
- `get_overdue_tasks()` → `List[Task]`
- `get_due_soon_tasks(hours_ahead: int = 24)` → `List[Task]`
- `get_recurring_tasks()` → `List[Task]`
- `process_completed_recurring_task(task_id: int)` → `Optional[Task]` (creates next instance if recurring)