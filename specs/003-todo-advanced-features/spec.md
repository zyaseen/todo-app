# Feature Specification: Todo Advanced Features

**Feature Branch**: `003-todo-advanced-features`
**Created**: 2026-01-05
**Status**: Draft
**Input**: User description: "Create a detailed functional and technical specification document EXCLUSIVELY for the ADVANCED LEVEL (Intelligent Features) of the Progressive Todo console application. Current state (after Intermediate level completion): - In-memory storage with list/dict of Task objects - Task model already includes: id, title, description, completed, priority (high/medium/low/None), tags (list[str]) - Full CLI commands exist: add, update, delete, list (with search/filter/sort), complete/toggle - Clean modular structure, type hints, docstrings, tests New requirements for Advanced Level — implement ONLY these two major feature groups: 1. Due Dates & Time Reminders - Add optional due_date field to Task: Optional[datetime.datetime] (or separate date + time) - Support setting due date/time when adding or updating a task → Accept formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, relative like "tomorrow 3pm", "next friday", "in 2 days" (simple parsing) - Display in list view: e.g. "due 2026-01-15 14:30" or "due tomorrow" + overdue warning (red/★ if past due) - Implement basic reminder system: - When user runs the app (or uses a new command like "check-reminders"), show all overdue + due-soon tasks (e.g. due in next 24h) - Optional: Desktop notification for overdue/due-soon tasks using plyer (cross-platform) if user runs a background checker mode - CLI extensions: - add/update: --due "2026-01-20 15:00" or --due "tomorrow 9am" - list: --overdue, --due-soon (next 24h), --due-today - New command: reminders (or check-reminders) — shows urgent items with notification option 2. Recurring Tasks - Add optional recurrence field to Task: Optional[dict] with pattern info → Supported patterns (minimal set): - daily - weekly (on specific weekday: mon, tue, ...) - monthly (on day of month) - yearly → Optional: end_date (stop after this date) or count (repeat X times) - When a recurring task is marked complete: - Do NOT delete it - Automatically create next instance with updated due_date according to pattern - Keep original task as "template" with recurrence info - Mark the completed instance as done and link to the series (optional) - Display in list view: recurring icon/symbol + next occurrence - CLI extensions: - add/update: --recurring daily / --recurring weekly:friday / --recurring monthly:15 - New flag for list: --show-recurring (show template + next instances) - Rule: Only generate next instance when current one is completed (not auto-create future ones in advance) Technical & Design Guidelines (must follow): - Update Task model with: due_datetime: Optional[datetime.datetime] recurrence: Optional[dict] # e.g. {"type": "weekly", "weekday": "monday", "end_date": Optional[datetime]} - Still keep in-memory approach (no database yet — but design for future easy migration) - Use python-dateutil or dateparser library for flexible due date input parsing (if allowed by project rules; otherwise implement simple parsing) - For desktop notifications: use plyer library (add as dependency if not present) - Background checking: optional simple loop mode (run app with --watch) that checks every X minutes and shows notifications - Never delete recurring templates — manage instances carefully - UX priorities: - Clear visual distinction for overdue (color/symbol), due soon, recurring - Helpful error messages for invalid date/recurrence inputs - Confirmation when creating next recurring instance Non-goals for this phase (do NOT implement): - Full calendar integration - Mobile push notifications - Email/SMS reminders - Complex natural language parsing beyond simple relative dates - Cloud sync / multi-device support - GUI (stay CLI) Deliver a precise specification document ready for planning and code generation, structured with: - Advanced phase goals & scope boundaries - Updated Task data model (new fields + example values) - Detailed CLI command extensions (flags, examples, output format) - Acceptance criteria for each feature group - Reminder & recurrence logic rules (flow diagrams in text) - New/updated tests needed (due date parsing, recurrence creation, overdue detection, notifications) Focus strictly on adding these intelligent features on top of existing code — minimize disruption to basic & intermediate functionality."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task with Due Date (Priority: P1)

As a user, I want to add tasks with due dates so that I can track deadlines and important time-sensitive activities.

**Why this priority**: This is the foundational feature for the due date functionality that enables users to set deadlines for their tasks.

**Independent Test**: The application allows users to add a new task with title, description, priority, tags, and due date (in various formats like YYYY-MM-DD, relative terms like "tomorrow 3pm"), assigns it a unique ID, and displays a confirmation message. The task appears in the list with the specified due date.

**Acceptance Scenarios**:

1. **Given** I am using the todo application, **When** I run `todo add "Submit quarterly report" --due "2026-01-20 15:00"`, **Then** a new task with ID is created with title "Submit quarterly report", due date set to 2026-01-20 15:00, and a success message is displayed.
2. **Given** I am using the todo application, **When** I run `todo add "Team meeting" --due "tomorrow 9am"`, **Then** a new task with ID is created with title "Team meeting", due date set to tomorrow at 9am, and a success message is displayed.

---

### User Story 2 - View Tasks with Due Dates and Reminders (Priority: P1)

As a user, I want to see tasks with their due dates and receive reminders for overdue or upcoming tasks so that I can manage my time effectively.

**Why this priority**: This is the core functionality that allows users to see and be reminded of their time-sensitive tasks.

**Independent Test**: The application displays tasks with their due dates, shows overdue tasks with warnings, highlights tasks due soon, and provides a command to check for urgent items.

**Acceptance Scenarios**:

1. **Given** I have tasks with various due dates, **When** I run `todo list --overdue`, **Then** only overdue tasks are displayed with clear visual indicators.
2. **Given** I have tasks due soon, **When** I run `todo list --due-soon`, **Then** only tasks due within the next 24 hours are displayed.
3. **Given** I have tasks with various due dates, **When** I run `todo reminders`, **Then** all overdue and due-soon tasks are displayed with urgency indicators.

---

### User Story 3 - Create Recurring Tasks (Priority: P2)

As a user, I want to create recurring tasks (daily, weekly, monthly, yearly) so that I don't have to repeatedly add routine activities.

**Why this priority**: This feature automates the creation of routine tasks, saving users time and effort.

**Independent Test**: The application allows users to add a recurring task with a specified pattern (daily, weekly, monthly, yearly), and when the task is completed, a new instance is automatically created according to the pattern.

**Acceptance Scenarios**:

1. **Given** I am using the todo application, **When** I run `todo add "Daily workout" --recurring daily`, **Then** a recurring task template is created with daily recurrence pattern.
2. **Given** I have a daily recurring task, **When** I mark it complete with `todo complete 1`, **Then** the current instance is marked complete and a new instance is created for the next day.

---

### User Story 4 - Manage Recurring Task Instances (Priority: P2)

As a user, I want to manage recurring task instances so that I can track and update specific occurrences of recurring tasks.

**Why this priority**: This allows users to handle specific instances of recurring tasks differently if needed.

**Independent Test**: The application allows users to update, delete, or mark specific instances of recurring tasks while preserving the template and future occurrences.

**Acceptance Scenarios**:

1. **Given** I have recurring tasks, **When** I run `todo list --show-recurring`, **Then** both the template and next scheduled instances are displayed.
2. **Given** I have a recurring task instance, **When** I run `todo update 5 --title "Updated weekly meeting"`, **Then** only that specific instance is updated, not the template or other instances.

---

### User Story 5 - Set and Receive Notifications (Priority: P3)

As a user, I want to receive notifications for overdue or due-soon tasks so that I don't miss important deadlines.

**Why this priority**: This provides proactive alerts to help users stay on top of their tasks.

**Independent Test**: The application provides desktop notifications for overdue or due-soon tasks when running in watch mode or when checking reminders.

**Acceptance Scenarios**:

1. **Given** I have overdue tasks, **When** I run `todo reminders --notify`, **Then** desktop notifications are displayed for each overdue task.
2. **Given** I run the application with watch mode, **When** tasks become overdue, **Then** desktop notifications are automatically shown.

---

### Edge Cases

- What happens when trying to add a task with an invalid date format?
- How does system handle recurring tasks with end dates that have passed?
- What happens when trying to list tasks when no tasks have due dates?
- How does system handle tasks with due dates in the past?
- What happens when trying to create a recurring task with an invalid pattern?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with optional due date/time in various formats (YYYY-MM-DD, YYYY-MM-DD HH:MM, relative terms like "tomorrow 3pm")
- **FR-002**: System MUST store due date as datetime object in Task model
- **FR-003**: System MUST display due dates in list view with clear formatting (e.g. "due 2026-01-15 14:30" or "due tomorrow")
- **FR-004**: System MUST highlight overdue tasks with visual indicators (red/★ symbol)
- **FR-005**: System MUST provide a reminders command to show overdue and due-soon tasks
- **FR-006**: System MUST allow filtering tasks by due date status (--overdue, --due-soon, --due-today)
- **FR-007**: System MUST support recurring tasks with patterns: daily, weekly, monthly, yearly
- **FR-008**: System MUST store recurrence information as a dictionary in Task model
- **FR-009**: System MUST create new task instance when a recurring task is marked complete
- **FR-010**: System MUST NOT delete recurring task templates when instances are completed
- **FR-011**: System MUST support optional end conditions for recurring tasks (end date or count)
- **FR-012**: System MUST provide --show-recurring flag to display templates and next instances
- **FR-013**: System MUST parse relative date expressions (tomorrow, next friday, in 2 days)
- **FR-014**: System MUST provide desktop notifications for overdue/due-soon tasks (using plyer)
- **FR-015**: System MUST validate date and recurrence inputs with helpful error messages

### Key Entities

- **Task**: Represents a single todo item with fields: id (int), title (str), description (str), completed (bool), priority (Optional[str]), tags (list[str]), due_datetime (Optional[datetime.datetime]), recurrence (Optional[dict])

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, update, and manage tasks with due dates and recurrence patterns with 100% success rate for valid inputs
- **SC-002**: System handles due date parsing and recurrence logic efficiently for lists up to 1000 tasks (response time < 1 second)
- **SC-003**: 95% of user actions result in clear, understandable feedback messages
- **SC-004**: All new advanced features are covered by unit tests with at least 90% code coverage
- **SC-005**: Users can create and manage recurring tasks with 100% accuracy in pattern execution
- **SC-006**: Notification system works reliably across different platforms (Windows, macOS, Linux)