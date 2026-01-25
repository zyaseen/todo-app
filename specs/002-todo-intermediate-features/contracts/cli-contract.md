# Todo CLI Extended API Contract

## Command Structure
```
todo <command> [arguments] [options]
```

## Extended Commands

### add
Add a new task to the list with optional priority and tags
```
todo add <title> [--desc DESCRIPTION] [--priority {high,medium,low}] [--tags TAGS]
```
- `title`: Required string, non-empty
- `--desc`: Optional string description
- `--priority`: Optional priority level (high, medium, low, or none)
- `--tags`: Optional comma-separated list of tags (e.g., "work,urgent,shopping")

### list
Display all tasks with filtering, searching, and sorting options
```
todo list [--search SEARCH] [--status {all,incomplete,completed}] [--priority {high,medium,low,none}] [--tag TAG] [--sort {created,alpha,priority,tags}] [--reverse]
```
- `--search`: Optional keyword to search in title or description
- `--status`: Optional filter by completion status (all, incomplete, completed)
- `--priority`: Optional filter by priority level (high, medium, low, none)
- `--tag`: Optional filter by tag presence
- `--sort`: Optional sort method (created, alpha, priority, tags)
- `--reverse`: Optional flag to reverse sort order

### update
Update an existing task with optional priority and tags
```
todo update <id> [--title TITLE] [--desc DESCRIPTION] [--priority {high,medium,low}] [--tags TAGS] [--add-tag TAG] [--remove-tag TAG]
```
- `id`: Required integer, existing task ID
- `--title`: Optional string for new title
- `--desc`: Optional string for new description
- `--priority`: Optional priority level (high, medium, low, or none)
- `--tags`: Optional comma-separated list of tags (replaces all tags)
- `--add-tag`: Optional single tag to add to existing tags
- `--remove-tag`: Optional single tag to remove from existing tags

### delete
Delete a task (unchanged from basic version)
```
todo delete <id>
```
- `id`: Required integer, existing task ID

### complete
Mark a task as complete (unchanged from basic version)
```
todo complete <id>
```
- `id`: Required integer, existing task ID

### incomplete
Mark a task as incomplete (unchanged from basic version)
```
todo incomplete <id>
```
- `id`: Required integer, existing task ID

## Exit Codes
- 0: Success
- 1: General error
- 2: Command-line usage error
- 3: Task not found error
- 4: Invalid priority value error

## Output Format
- Success messages: Plain text confirmation
- Task listing: Formatted with rich library showing ID, priority indicator, tags, title, description, and status indicator ([ ] or [x])
- Error messages: Plain text with descriptive error