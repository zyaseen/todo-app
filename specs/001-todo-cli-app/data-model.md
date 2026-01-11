# Data Model: Todo CLI Application

## Task Entity

### Fields
- **id**: `int` - Unique sequential identifier assigned when task is created
- **title**: `str` - Required title of the task (non-empty string validation required)
- **description**: `str` - Optional description of the task (can be empty)
- **completed**: `bool` - Boolean indicating completion status (default: False)

### Validation Rules
- `title` must be a non-empty string (length > 0)
- `id` must be unique within the application session
- `id` must be a positive integer (≥ 1)

### State Transitions
- `completed` state can transition from `False` to `True` (incomplete → complete)
- `completed` state can transition from `True` to `False` (complete → incomplete)

## TodoList Entity

### Fields
- **tasks**: `List[Task]` - Collection of Task objects stored in memory
- **next_id**: `int` - Next available ID to assign to a new task (starts at 1)

### Validation Rules
- No two tasks can have the same ID
- Task IDs must be sequential and positive integers
- When a task is deleted, its ID is not reused

### Operations
- `add_task(title: str, description: str = "")` → `Task`
- `get_all_tasks()` → `List[Task]`
- `get_task_by_id(task_id: int)` → `Optional[Task]`
- `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None)` → `bool`
- `delete_task(task_id: int)` → `bool`
- `mark_task_complete(task_id: int)` → `bool`
- `mark_task_incomplete(task_id: int)` → `bool`