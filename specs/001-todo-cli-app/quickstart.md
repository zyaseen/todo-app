# Quickstart Guide: Todo CLI Application

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

## Usage Examples

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
- Run unit tests: `pytest tests/unit/`
- Run integration tests: `pytest tests/integration/`
- Run all tests: `pytest`