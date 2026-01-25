# Data Model: Todo Intermediate Features

## Extended Task Entity

### Fields
- **id**: `int` - Unique sequential identifier assigned when task is created
- **title**: `str` - Required title of the task (non-empty string validation required)
- **description**: `str` - Optional description of the task (can be empty)
- **completed**: `bool` - Boolean indicating completion status (default: False)
- **priority**: `Optional[str]` - Priority level of the task: "high", "medium", "low", or None (default: None)
- **tags**: `list[str]` - List of tags associated with the task (default: empty list)

### Validation Rules
- `title` must be a non-empty string (length > 0)
- `id` must be unique within the application session
- `id` must be a positive integer (≥ 1)
- `priority` must be one of: "high", "medium", "low", or None
- `tags` must be a list of strings (no validation on tag content format)

### State Transitions
- `completed` state can transition from `False` to `True` (incomplete → complete)
- `completed` state can transition from `True` to `False` (complete → incomplete)
- `priority` can be updated to any valid value
- `tags` can be added, removed, or replaced

## Extended TodoList Entity

### Fields
- **tasks**: `List[Task]` - Collection of Task objects stored in memory
- **next_id**: `int` - Next available ID to assign to a new task (starts at 1)

### Validation Rules
- No two tasks can have the same ID
- Task IDs must be sequential and positive integers
- When a task is deleted, its ID is not reused

### Operations
- `add_task(title: str, description: str = "", priority: Optional[str] = None, tags: list[str] = [])` → `Task`
- `get_all_tasks()` → `List[Task]`
- `get_task_by_id(task_id: int)` → `Optional[Task]`
- `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None)` → `bool`
- `delete_task(task_id: int)` → `bool`
- `mark_task_complete(task_id: int)` → `bool`
- `mark_task_incomplete(task_id: int)` → `bool`
- `search_tasks(keyword: str)` → `List[Task]`
- `filter_tasks(status: Optional[str] = None, priority: Optional[str] = None, tag: Optional[str] = None)` → `List[Task]`
- `sort_tasks(sort_by: str, reverse: bool = False)` → `List[Task]`
- `combine_filters_search(search_keyword: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None, tag: Optional[str] = None, sort_by: Optional[str] = None, reverse: bool = False)` → `List[Task]`

### Priority Ordering
- High → Medium → Low → None (used for sorting)