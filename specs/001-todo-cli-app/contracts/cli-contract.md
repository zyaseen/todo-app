# Todo CLI API Contract

## Command Structure
```
todo <command> [arguments] [options]
```

## Commands

### add
Add a new task to the list
```
todo add <title> [--desc DESCRIPTION]
```
- `title`: Required string, non-empty
- `--desc`: Optional string description

### list
Display all tasks
```
todo list
```

### update
Update an existing task
```
todo update <id> [--title TITLE] [--desc DESCRIPTION]
```
- `id`: Required integer, existing task ID
- `--title`: Optional string
- `--desc`: Optional string

### delete
Delete a task
```
todo delete <id>
```
- `id`: Required integer, existing task ID

### complete
Mark a task as complete
```
todo complete <id>
```
- `id`: Required integer, existing task ID

### incomplete
Mark a task as incomplete
```
todo incomplete <id>
```
- `id`: Required integer, existing task ID

## Exit Codes
- 0: Success
- 1: General error
- 2: Command-line usage error
- 3: Task not found error

## Output Format
- Success messages: Plain text confirmation
- Task listing: Formatted with rich library showing ID, title, description, and status indicator ([ ] or [x])
- Error messages: Plain text with descriptive error