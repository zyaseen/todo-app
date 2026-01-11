# Todo CLI Application

A simple command-line todo application built with Python that allows you to manage your tasks efficiently.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with status indicators
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- All data stored in memory (no persistence)

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
```

### Listing Tasks
```bash
python -m todo list
```

### Updating a Task
```bash
python -m todo update 1 --title "Buy groceries and cook dinner"
python -m todo update 1 --desc "Milk, eggs, and bread"
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