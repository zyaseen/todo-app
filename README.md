# Todo CLI Application

A simple command-line todo application built with Python that allows you to manage your tasks efficiently.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with status indicators
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- All data stored in memory (no persistence)
- NEW: Priorities (high, medium, low)
- NEW: Tags for categorization
- NEW: Search and filter functionality
- NEW: Sort tasks by various criteria

## Installation

1. Clone the repository
2. Make sure you have Python 3.13+ installed
3. Install dependencies:
   ```bash
   pip install rich pytest
   ```

## Usage

### Adding a Task
```bash
python -m todo add "Buy groceries"
# or with description
python -m todo add "Complete project" --desc "Finish the specification document"
# or with priority and tags
python -m todo add "Prepare quarterly report" --priority high --tags "work,urgent"
```

### Listing Tasks
```bash
python -m todo list
# with filters and sorting
python -m todo list --priority high --status incomplete
python -m todo list --search "groceries" --sort alpha
python -m todo list --tag work --sort priority
```

### Updating a Task
```bash
python -m todo update 1 --title "Buy groceries and cook dinner"
python -m todo update 1 --desc "Milk, eggs, and bread"
python -m todo update 1 --priority medium --tags "shopping,home"
python -m todo update 1 --add-tag "important"  # Add a single tag
python -m todo update 1 --remove-tag "work"    # Remove a single tag
```

### Deleting a Task
```bash
python -m todo delete 1
```

### Marking Tasks Complete/Incomplete
```bash
python -m todo complete 1
python -m todo incomplete 1
```

### Available Filters and Sorting Options
- `--search KEYWORD`: Search for keyword in title or description
- `--status {all,incomplete,completed}`: Filter by completion status
- `--priority {high,medium,low,none}`: Filter by priority level
- `--tag TAG`: Filter by tag presence
- `--sort {created,alpha,priority,tags}`: Sort by specified criteria
- `--reverse`: Reverse sort order

## Development

### Running Tests
```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/
```

## Architecture

The application follows a modular design:

- `src/todo/task.py`: Defines the Task dataclass
- `src/todo/todo_list.py`: Manages the collection of tasks
- `src/todo/cli.py`: Handles command-line interface and argument parsing
- `src/todo/errors.py`: Contains custom exception classes
- `tests/`: Contains unit and integration tests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request