# Tasks: Todo Advanced Features

**Input**: Design documents from `/specs/003-todo-advanced-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are required for all new advanced features (due dates, recurrence, reminders, notifications) per the specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Install new dependencies (dateparser, plyer) using UV as specified in implementation plan
- [ ] T002 [P] Update Task dataclass in src/todo/task.py with due_datetime and recurrence fields
- [ ] T003 [P] Update CLI argument parser in src/todo/cli.py with new command options for due dates and recurrence

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Implement date parsing utilities in src/todo/utils.py for flexible date input (relative dates like "tomorrow", "next friday")
- [ ] T005 Update TodoList class in src/todo/todo_list.py with methods for handling due dates (get_overdue_tasks, get_due_soon_tasks)
- [ ] T006 [P] Update TodoList class in src/todo/todo_list.py with methods for handling recurrence (process_completed_recurring_task, get_recurring_tasks)
- [ ] T007 Implement notification system in src/todo/notifications.py using plyer for cross-platform desktop notifications
- [ ] T008 Update Task validation to handle new due_datetime and recurrence fields in src/todo/task.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task with Due Date (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with due dates in various formats so that they can track deadlines and important time-sensitive activities.

**Independent Test**: The application allows users to add a new task with title, description, priority, tags, and due date (in various formats like YYYY-MM-DD, relative terms like "tomorrow 3pm"), assigns it a unique ID, and displays a confirmation message. The task appears in the list with the specified due date.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Unit test for Task creation with due date in tests/unit/test_task.py
- [ ] T010 [P] [US1] Unit test for TodoList.add_task() with due date in tests/unit/test_todo_list.py
- [ ] T011 [P] [US1] Integration test for CLI add command with --due flag in tests/integration/test_cli.py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Extend CLI add command to accept --due flag in src/todo/cli.py
- [ ] T013 [US1] Update CLI add command handler to process due date input in src/todo/cli.py
- [ ] T014 [US1] Add date validation and parsing for add command in src/todo/cli.py
- [ ] T015 [US1] Update task display format to show due dates in src/todo/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks with Due Dates and Reminders (Priority: P1)

**Goal**: Enable users to see tasks with their due dates and receive reminders for overdue or upcoming tasks so that they can manage their time effectively.

**Independent Test**: The application displays tasks with their due dates, shows overdue tasks with warnings, highlights tasks due soon, and provides a command to check for urgent items.

### Tests for User Story 2 (REQUIRED) ⚠️

- [ ] T016 [P] [US2] Unit test for TodoList.get_overdue_tasks() in tests/unit/test_todo_list.py
- [ ] T017 [P] [US2] Unit test for TodoList.get_due_soon_tasks() in tests/unit/test_todo_list.py
- [ ] T018 [P] [US2] Integration test for CLI list command with --overdue, --due-soon, --due-today flags in tests/integration/test_cli.py
- [ ] T019 [P] [US2] Integration test for CLI reminders command in tests/integration/test_cli.py

### Implementation for User Story 2

- [ ] T020 [P] [US2] Extend CLI list command to accept --overdue flag in src/todo/cli.py
- [ ] T021 [P] [US2] Extend CLI list command to accept --due-soon flag in src/todo/cli.py
- [ ] T022 [P] [US2] Extend CLI list command to accept --due-today flag in src/todo/cli.py
- [ ] T023 [US2] Implement CLI reminders command handler in src/todo/cli.py
- [ ] T024 [US2] Update task display format to show overdue warnings in src/todo/cli.py
- [ ] T025 [US2] Add message when no tasks match due date filters in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Create Recurring Tasks (Priority: P2)

**Goal**: Enable users to create recurring tasks (daily, weekly, monthly, yearly) so that they don't have to repeatedly add routine activities.

**Independent Test**: The application allows users to add a recurring task with a specified pattern (daily, weekly, monthly, yearly), and when the task is completed, a new instance is automatically created according to the pattern.

### Tests for User Story 3 (REQUIRED) ⚠️

- [ ] T026 [P] [US3] Unit test for TodoList.add_task() with recurrence pattern in tests/unit/test_todo_list.py
- [ ] T027 [P] [US3] Unit test for TodoList.process_completed_recurring_task() in tests/unit/test_todo_list.py
- [ ] T028 [P] [US3] Integration test for CLI add command with --recurring flag in tests/integration/test_cli.py

### Implementation for User Story 3

- [ ] T029 [P] [US3] Extend CLI add command to accept --recurring flag in src/todo/cli.py
- [ ] T030 [US3] Update CLI add command handler to process recurrence pattern in src/todo/cli.py
- [ ] T031 [US3] Add recurrence validation for add command in src/todo/cli.py
- [ ] T032 [US3] Update task display format to show recurrence indicators in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Manage Recurring Task Instances (Priority: P2)

**Goal**: Enable users to manage recurring task instances so that they can track and update specific occurrences of recurring tasks.

**Independent Test**: The application allows users to update, delete, or mark specific instances of recurring tasks while preserving the template and future occurrences.

### Tests for User Story 4 (REQUIRED) ⚠️

- [ ] T033 [P] [US4] Unit test for updating recurring task instances in tests/unit/test_todo_list.py
- [ ] T034 [P] [US4] Integration test for CLI list command with --show-recurring flag in tests/integration/test_cli.py

### Implementation for User Story 4

- [ ] T035 [P] [US4] Extend CLI list command to accept --show-recurring flag in src/todo/cli.py
- [ ] T036 [US4] Update CLI list command handler to show recurring templates and instances in src/todo/cli.py
- [ ] T037 [US4] Update CLI update command to work with recurring task instances in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Notifications (Priority: P3)

**Goal**: Enable users to receive notifications for overdue or due-soon tasks so that they don't miss important deadlines.

**Independent Test**: The application provides desktop notifications for overdue or due-soon tasks when running in watch mode or when checking reminders.

### Tests for User Story 5 (REQUIRED) ⚠️

- [ ] T038 [P] [US5] Unit test for notification system in tests/unit/test_notifications.py
- [ ] T039 [P] [US5] Integration test for CLI reminders command with --notify flag in tests/integration/test_cli.py

### Implementation for User Story 5

- [ ] T040 [P] [US5] Extend CLI reminders command to accept --notify flag in src/todo/cli.py
- [ ] T041 [US5] Update CLI reminders command handler to trigger notifications in src/todo/cli.py

**Checkpoint**: All user stories should now be independently functional

---

### Edge Cases & Error Handling

**Goal**: Handle all specified edge cases and error conditions

**Independent Test**: The application properly handles all edge cases and provides user-friendly error messages.

#### Tests for Edge Cases (REQUIRED) ⚠️

- [ ] T042 [P] [EDGE] Unit test for invalid date format handling in tests/unit/test_utils.py
- [ ] T043 [P] [EDGE] Unit test for invalid recurrence pattern handling in tests/unit/test_todo_list.py
- [ ] T044 [P] [EDGE] Integration test for error conditions in tests/integration/test_cli.py

#### Implementation for Edge Cases

- [ ] T045 [P] [EDGE] Implement validation for date formats in src/todo/utils.py
- [ ] T046 [EDGE] Implement validation for recurrence patterns in src/todo/todo_list.py
- [ ] T047 [EDGE] Add appropriate error messages for invalid inputs in src/todo/cli.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T048 [P] Update README.md with new command examples for due dates and recurring tasks
- [ ] T049 Code cleanup and refactoring
- [ ] T050 Performance optimization for date-based operations
- [ ] T051 [P] Additional unit tests in tests/unit/ to achieve 90%+ coverage
- [ ] T052 Security hardening
- [ ] T053 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Edge Cases**: Depends on all user stories being implemented
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task creation with due date in tests/unit/test_task.py"
Task: "Unit test for TodoList.add_task() with due date in tests/unit/test_todo_list.py"
Task: "Integration test for CLI add command with --due flag in tests/integration/test_cli.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Extend CLI add command to accept --due flag in src/todo/cli.py"
Task: "Update CLI add command handler to process due date input in src/todo/cli.py"
Task: "Add date validation and parsing for add command in src/todo/cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence