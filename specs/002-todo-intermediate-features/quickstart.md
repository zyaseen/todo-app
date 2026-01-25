# Quickstart Guide: Todo Intermediate Features

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
3. Install the package in development mode:
   ```bash
   uv build
   ```

## New Usage Examples

### Adding a Task with Priority and Tags
```bash
python -m todo add "Prepare quarterly report" --priority high --tags "work,urgent"
python -m todo add "Buy groceries" --priority low --tags "shopping,home"
```

### Listing Tasks with Filters and Sorting
```bash
# Filter by priority
python -m todo list --priority high

# Filter by completion status
python -m todo list --status incomplete

# Filter by tag
python -m todo list --tag work

# Search tasks
python -m todo list --search "report"

# Sort tasks by priority
python -m todo list --sort priority

# Combine filters and sorting
python -m todo list --status incomplete --priority high --sort created
```

### Updating a Task's Priority and Tags
```bash
python -m todo update 1 --priority medium
python -m todo update 1 --tags "personal,family,vacation"
python -m todo update 1 --add-tag "important"  # Add individual tag
python -m todo update 1 --remove-tag "work"    # Remove individual tag
```

## Development
- Run unit tests: `pytest tests/unit/`
- Run integration tests: `pytest tests/integration/`
- Run all tests: `pytest`