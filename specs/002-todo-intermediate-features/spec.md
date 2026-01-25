# Feature Specification: Todo Intermediate Features

**Feature Branch**: `002-todo-intermediate-features`
**Created**: 2026-01-05
**Status**: Draft
**Input**: User description: "Create a detailed functional and technical specification document exclusively for the INTERMEDIATE LEVEL of the Progressive Todo application. This specification ONLY covers the new features of the Intermediate phase. Assume Phase I (Basic Level) is already implemented and working: - In-memory storage - Core features: add (title + description), list/view, update title/desc, delete by id, mark complete/incomplete - Current Task model: id, title, description, completed New requirements for Intermediate Level (Organization & Usability): Must implement exactly these four feature groups: 1. Priorities - Each task can have one priority level: high, medium, low (or none) - Priority should be optional (default: none/medium?) - Display priority in list view (e.g. [H], [M], [L] or colored emoji/symbol) - Allow setting/updating priority when adding or updating a task 2. Tags / Categories - Tasks can have zero or multiple tags/categories (free text labels) - Examples: work, home, urgent, shopping, personal, projectX - Support adding/removing tags during task creation and update - Display tags in list view (compact, e.g. #work #urgent) 3. Search & Filter - Search by keyword (matches title or description, case-insensitive, partial match) - Filter by: - completion status (all / incomplete / completed) - priority (high / medium / low / none) - tags (contains specific tag) - Should be combinable (e.g. show incomplete high-priority tasks containing "report") 4. Sort Tasks - Multiple sort options for the list view: - By creation order (default, newest/oldest first) - Alphabetically by title - By priority (high → medium → low → none) - By number of tags (most → least) - Sort should be selectable via command-line option/argument Technical & Design Guidelines (must follow): - Update the Task data model to include new fields: priority: Optional[str] # "high", "medium", "low" or None tags: list[str] # default empty list - Keep in-memory storage (same list/dict as Phase I) - Extend existing CLI commands sensibly: - `add` should accept --priority and --tags "work,urgent" - `update` should allow changing priority and tags - `list` should accept flags like --search "keyword" --filter-incomplete --priority high --tag work --sort priority - Maintain clean architecture: - Keep data model (Task) separate from business logic (TodoManager) and presentation (CLI) - Add helper methods for filtering, searching, sorting - UX requirements: - Clear, compact list formatting showing new fields - Helpful messages when no tasks match filter/search - Input validation for priority values - Testing: - Add pytest cases specifically covering new fields, filtering logic, search matching, sorting orders, and combinations Non-goals for this phase (do NOT implement): - Due dates, recurring tasks, persistence, reminders, notifications - Any advanced visualization (colors beyond simple symbols) - Task reordering (manual drag-and-drop style) Deliver a clear, unambiguous specification document ready for planning and code generation, structured with: - Overview of Intermediate phase goals - Updated data model - Detailed command-line interface specification (commands, flags, examples) - Acceptance criteria per feature group - Expected output format examples - List of new/updated tests needed Focus only on adding these organization & usability improvements — do not redesign the entire application."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task with Priority and Tags (Priority: P1)

As a user, I want to add tasks with priority levels and tags so that I can better organize and categorize my tasks.

**Why this priority**: This enhances the basic add functionality by allowing users to add organizational metadata at creation time, making tasks more manageable from the start.

**Independent Test**: The application allows users to add a new task with title, description, priority level (high/medium/low/none), and tags (comma-separated list), assigns it a unique ID, and displays a confirmation message. The task appears in the list with the specified priority and tags.

**Acceptance Scenarios**:

1. **Given** I am using the todo application, **When** I run `todo add "Prepare quarterly report" --priority high --tags "work,urgent"`, **Then** a new task with ID is created with title "Prepare quarterly report", priority "high", and tags ["work", "urgent"], and a success message is displayed.
2. **Given** I am using the todo application, **When** I run `todo add "Buy groceries" --priority low --tags "shopping,home"`, **Then** a new task with ID is created with title "Buy groceries", priority "low", and tags ["shopping", "home"], and a success message is displayed.

---

### User Story 2 - List Tasks with Filtering and Sorting (Priority: P1)

As a user, I want to filter and sort my tasks so that I can focus on the most important or relevant ones.

**Why this priority**: This is the core enhancement to the list functionality that allows users to manage larger task lists more effectively by focusing on subsets of interest.

**Independent Test**: The application displays filtered and sorted tasks with their ID, title, description (or "No description"), priority indicator, tags, and status indicator ([ ] for incomplete, [x] for complete).

**Acceptance Scenarios**:

1. **Given** I have tasks with various priorities and completion statuses, **When** I run `todo list --filter-priority high --filter-status incomplete`, **Then** only incomplete high-priority tasks are displayed.
2. **Given** I have tasks with various tags, **When** I run `todo list --tag work --sort priority`, **Then** tasks tagged with "work" are displayed sorted by priority (high to low).
3. **Given** I have tasks with various titles, **When** I run `todo list --search "report" --sort alpha`, **Then** tasks containing "report" in title or description are displayed alphabetically by title.

---

### User Story 3 - Update Task Priority and Tags (Priority: P2)

As a user, I want to update the priority and tags of existing tasks so that I can adjust their importance and categorization as needed.

**Why this priority**: This allows users to reorganize and reprioritize tasks as circumstances change, maintaining the relevance of their organizational system.

**Independent Test**: The application allows users to update the priority and/or tags of an existing task by ID, changing these attributes, and confirms the update.

**Acceptance Scenarios**:

1. **Given** I have a task with ID 1 and no priority/tags, **When** I run `todo update 1 --priority high --tags "work,urgent"`, **Then** the task priority is updated to "high", tags are set to ["work", "urgent"], and a success message is displayed.
2. **Given** I have a task with ID 1 and existing tags, **When** I run `todo update 1 --tags "personal,family"`, **Then** the task tags are updated to ["personal", "family"], and a success message is displayed.

---

### User Story 4 - Search Tasks by Keyword (Priority: P2)

As a user, I want to search for tasks by keyword so that I can quickly find specific tasks among many.

**Why this priority**: This significantly improves the usability of the application when users have many tasks and need to find specific ones quickly.

**Independent Test**: The application searches through task titles and descriptions for the specified keyword and displays matching tasks.

**Acceptance Scenarios**:

1. **Given** I have tasks with various titles and descriptions, **When** I run `todo list --search "groceries"`, **Then** all tasks with "groceries" in title or description are displayed.
2. **Given** I have no tasks matching the search term, **When** I run `todo list --search "nonexistent"`, **Then** a message "No tasks match your search" is displayed.

---

### User Story 5 - Combined Filter Operations (Priority: P3)

As a user, I want to combine multiple filters (priority, status, tags, search) so that I can create complex queries to find exactly what I need.

**Why this priority**: This provides maximum flexibility for power users who need to create sophisticated views of their task list.

**Independent Test**: The application applies multiple filters simultaneously and displays only tasks that match all specified criteria.

**Acceptance Scenarios**:

1. **Given** I have tasks with various attributes, **When** I run `todo list --filter-status incomplete --priority high --tag work`, **Then** only incomplete, high-priority tasks tagged with "work" are displayed.
2. **Given** I have tasks with various attributes, **When** I run `todo list --search "report" --filter-status complete --sort alpha`, **Then** only completed tasks containing "report" are displayed, sorted alphabetically.

---

### Edge Cases

- What happens when trying to add a task with an invalid priority value?
- How does system handle filtering with non-existent tags?
- What happens when trying to list tasks when no tasks match the filter criteria?
- How does system handle empty search queries?
- What happens when trying to sort an empty filtered list?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with optional priority (high, medium, low, none) and tags (list of strings)
- **FR-002**: System MUST display priority indicators in list view (e.g., [H], [M], [L], [N])
- **FR-003**: System MUST display tags in list view (e.g., #work #urgent)
- **FR-004**: System MUST allow filtering tasks by completion status (all, incomplete, completed)
- **FR-005**: System MUST allow filtering tasks by priority (high, medium, low, none, all)
- **FR-006**: System MUST allow filtering tasks by tag presence
- **FR-007**: System MUST allow searching tasks by keyword in title or description
- **FR-008**: System MUST allow sorting tasks by creation order (newest/oldest)
- **FR-009**: System MUST allow sorting tasks alphabetically by title
- **FR-010**: System MUST allow sorting tasks by priority (high → medium → low → none)
- **FR-011**: System MUST allow sorting tasks by number of tags (most → least)
- **FR-012**: System MUST allow combining multiple filters and search criteria
- **FR-013**: System MUST allow updating task priority and tags via update command
- **FR-014**: System MUST validate priority values (accept only high, medium, low, none)
- **FR-015**: System MUST handle case-insensitive search and filtering
- **FR-016**: System MUST provide clear feedback when no tasks match filter/search criteria

### Key Entities

- **Task**: Represents a single todo item with fields: id (int), title (str), description (str), completed (bool), priority (Optional[str]), tags (list[str])

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, update, filter, search, and sort tasks with 100% success rate for valid inputs
- **SC-002**: System handles filtering and sorting operations efficiently for lists up to 1000 tasks (response time < 1 second)
- **SC-003**: 95% of user actions result in clear, understandable feedback messages
- **SC-004**: All new features are covered by unit tests with at least 90% code coverage
- **SC-005**: Users can combine multiple filters and search criteria with 100% accuracy
- **SC-006**: Search functionality returns relevant results with >90% precision