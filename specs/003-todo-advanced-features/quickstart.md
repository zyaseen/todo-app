# Quickstart Guide: Todo Advanced Features

## Prerequisites
- Python 3.13+
- UV package manager
- dateparser library (`pip install dateparser`)
- plyer library (`pip install plyer`)

## Setup
1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv add dateparser plyer
   ```
3. Install the package in development mode:
   ```bash
   uv build
   ```

## Advanced Usage Examples

### Adding Tasks with Due Dates
```bash
# Add a task with a specific due date and time
uv run main.py add "Submit quarterly report" --due "2026-01-20 15:00"

# Add a task with a relative due date
uv run main.py add "Team meeting" --due "tomorrow 9am"

# Add a task with due date, priority and tags
uv run main.py add "Prepare presentation" --due "next friday 2pm" --priority high --tags "work,urgent"
```

### Working with Recurring Tasks
```bash
# Add a daily recurring task
uv run main.py add "Morning meditation" --recurring daily

# Add a weekly recurring task for Fridays
uv run main.py add "Weekly team sync" --recurring weekly:friday

# Add a monthly recurring task on the 15th
uv run main.py add "Pay rent" --recurring monthly:15
```

### Filtering Tasks by Due Date
```bash
# List all overdue tasks
uv run main.py list --overdue

# List tasks due soon (within 24 hours)
uv run main.py list --due-soon

# List tasks due today
uv run main.py list --due-today

# List recurring tasks
uv run main.py list --show-recurring
```

### Checking Reminders
```bash
# Check for overdue and due-soon tasks
uv run main.py reminders

# Check reminders with notifications
uv run main.py reminders --notify
```

### Interactive Mode
```bash
# Run the interactive application
uv run main.py

# Use the menu to navigate:
# 1. Add Task (with due date and recurrence)
# 2. List Tasks (with filtering options)
# 3. Update Task
# 4. Delete Task
# 5. Mark Task Complete
# 6. Mark Task Incomplete
# 7. Exit
```

## Development
- Run unit tests: `pytest tests/unit/`
- Run integration tests: `pytest tests/integration/`
- Run all tests: `pytest`
- Test new advanced features: `pytest tests/ -k "due_date or recurrence or reminder"`