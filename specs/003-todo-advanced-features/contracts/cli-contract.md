# Todo CLI Advanced Features API Contract

## Command Structure
```
todo <command> [arguments] [options]
```

## Extended Commands

### add
Add a new task with optional due date and recurrence pattern
```
todo add <title> [--desc DESCRIPTION] [--priority {high,medium,low}] [--tags TAGS] [--due DUE_DATE] [--recurring RECURRENCE_PATTERN]
```
- `title`: Required string, non-empty
- `--desc`: Optional string description
- `--priority`: Optional priority level (high, medium, low)
- `--tags`: Optional comma-separated list of tags (e.g., "work,urgent,shopping")
- `--due`: Optional due date/time in various formats (YYYY-MM-DD, YYYY-MM-DD HH:MM, relative like "tomorrow 3pm", "next friday")
- `--recurring`: Optional recurrence pattern (daily, weekly:weekday, monthly:day, yearly)

### list
Display all tasks with optional filtering by due date and recurrence
```
todo list [--overdue] [--due-soon] [--due-today] [--show-recurring] [--status {all,incomplete,completed}] [--priority {high,medium,low,none}] [--tag TAG] [--sort {created,alpha,priority,tags}] [--reverse]
```
- `--overdue`: Show only overdue tasks
- `--due-soon`: Show only tasks due within 24 hours
- `--due-today`: Show only tasks due today
- `--show-recurring`: Show recurring task templates and next instances
- Other options as in previous phases

### update
Update an existing task with optional due date and recurrence changes
```
todo update <id> [--title TITLE] [--desc DESCRIPTION] [--priority {high,medium,low,none}] [--tags TAGS] [--add-tag TAG] [--remove-tag TAG] [--due DUE_DATE] [--recurring RECURRENCE_PATTERN]
```
- `id`: Required integer, existing task ID
- Other options as in previous phases
- `--due`: New due date/time (same formats as add command)
- `--recurring`: New recurrence pattern (same formats as add command)

### reminders
Show overdue and due-soon tasks with optional notifications
```
todo reminders [--notify]
```
- `--notify`: Optional flag to show desktop notifications for overdue/due-soon tasks

### complete
Mark a task as complete (enhanced to handle recurring tasks)
```
todo complete <id>
```
- `id`: Required integer, existing task ID
- If the task is recurring, creates the next instance according to the recurrence pattern

## Exit Codes
- 0: Success
- 1: General error
- 2: Command-line usage error
- 3: Task not found error
- 4: Invalid date/recurrence pattern error

## Output Format
- Success messages: Plain text confirmation with rich formatting
- Task listing: Formatted with rich library showing ID, priority indicator, tags, status indicator ([ ] or [x]), due date (if applicable), and recurrence indicator (if applicable)
- Error messages: Plain text with descriptive error
- Reminder notifications: Desktop notifications via plyer when --notify flag is used