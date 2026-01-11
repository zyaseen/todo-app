---

description: "Task list for Todo CLI Application"
---

# Tasks: Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are required for all 5 core features and edge cases per the specification.

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

- [X] T001 Create project structure per implementation plan with src/todo/ and tests/ directories
- [X] T002 Initialize Python project with proper dependencies (argparse, rich, pytest)
- [ ] T003 [P] Configure linting and formatting tools for PEP 8 compliance

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task dataclass in src/todo/task.py with id, title, description, completed fields
- [X] T005 Create TodoList class in src/todo/todo_list.py with all required operations
- [X] T006 [P] Set up pytest configuration and test directory structure
- [X] T007 Implement error handling base classes in src/todo/errors.py
- [X] T008 Create CLI argument parser in src/todo/cli.py with all required subcommands

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with required title and optional description, assigning unique incremental IDs

**Independent Test**: The application allows users to add a new task with a title and optional description, assigns it a unique ID, and displays a confirmation message. The task appears in the list when viewed.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for Task creation with required fields in tests/unit/test_task.py
- [X] T010 [P] [US1] Unit test for TodoList.add_task() in tests/unit/test_todo_list.py
- [X] T011 [P] [US1] Integration test for CLI add command in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Task dataclass validation for non-empty title in src/todo/task.py
- [X] T013 [US1] Implement TodoList.add_task() method with ID assignment in src/todo/todo_list.py
- [X] T014 [US1] Implement CLI add command handler in src/todo/cli.py
- [X] T015 [US1] Add input validation for add command in src/todo/cli.py
- [X] T016 [US1] Add success message output for add command using rich in src/todo/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View/List All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with ID, title, description (or "No description"), and status indicator ([ ] for incomplete, [x] for complete)

**Independent Test**: The application displays all tasks with their ID, title, description (or "No description" if empty), and status indicator ([ ] for incomplete, [x] for complete).

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T017 [P] [US2] Unit test for TodoList.get_all_tasks() in tests/unit/test_todo_list.py
- [X] T018 [P] [US2] Integration test for CLI list command in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T019 [P] [US2] Implement TodoList.get_all_tasks() method in src/todo/todo_list.py
- [X] T020 [US2] Implement CLI list command handler in src/todo/cli.py
- [X] T021 [US2] Format output with rich for consistent status indicators in src/todo/cli.py
- [X] T022 [US2] Handle empty task list case with "No tasks found" message in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Existing Task (Priority: P2)

**Goal**: Enable users to update the title and/or description of an existing task by its ID

**Independent Test**: The application allows users to update an existing task by ID, changing the title and/or description, and confirms the update.

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T023 [P] [US3] Unit test for TodoList.update_task() in tests/unit/test_todo_list.py
- [X] T024 [P] [US3] Integration test for CLI update command in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement TodoList.update_task() method in src/todo/todo_list.py
- [X] T026 [US3] Implement CLI update command handler in src/todo/cli.py
- [X] T027 [US3] Add input validation for update command in src/todo/cli.py
- [X] T028 [US3] Add success message output for update command in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Enable users to delete a task by its ID

**Independent Test**: The application allows users to delete a task by its ID and confirms the deletion.

### Tests for User Story 4 (REQUIRED) ⚠️

- [X] T029 [P] [US4] Unit test for TodoList.delete_task() in tests/unit/test_todo_list.py
- [X] T030 [P] [US4] Integration test for CLI delete command in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T031 [P] [US4] Implement TodoList.delete_task() method in src/todo/todo_list.py
- [X] T032 [US4] Implement CLI delete command handler in src/todo/cli.py
- [X] T033 [US4] Add input validation for delete command in src/todo/cli.py
- [X] T034 [US4] Add success message output for delete command in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark a task as complete or incomplete by its ID

**Independent Test**: The application allows users to toggle or set the completion status of a task by its ID and confirms the change.

### Tests for User Story 5 (REQUIRED) ⚠️

- [X] T035 [P] [US5] Unit test for TodoList.mark_task_complete() in tests/unit/test_todo_list.py
- [X] T036 [P] [US5] Unit test for TodoList.mark_task_incomplete() in tests/unit/test_todo_list.py
- [X] T037 [P] [US5] Integration test for CLI complete/incomplete commands in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T038 [P] [US5] Implement TodoList.mark_task_complete() method in src/todo/todo_list.py
- [X] T039 [P] [US5] Implement TodoList.mark_task_incomplete() method in src/todo/todo_list.py
- [X] T040 [US5] Implement CLI complete command handler in src/todo/cli.py
- [X] T041 [US5] Implement CLI incomplete command handler in src/todo/cli.py
- [X] T042 [US5] Add success message output for complete/incomplete commands in src/todo/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Edge Cases & Error Handling

**Goal**: Handle all specified edge cases and error conditions

**Independent Test**: The application properly handles all edge cases and provides user-friendly error messages.

### Tests for Edge Cases (REQUIRED) ⚠️

- [X] T043 [P] [EDGE] Unit test for empty title validation in tests/unit/test_task.py
- [X] T044 [P] [EDGE] Unit test for invalid task ID handling in tests/unit/test_todo_list.py
- [X] T045 [P] [EDGE] Integration test for invalid command arguments in tests/integration/test_cli.py

### Implementation for Edge Cases

- [X] T046 [P] [EDGE] Implement empty title validation in src/todo/task.py
- [X] T047 [EDGE] Implement invalid task ID handling in src/todo/todo_list.py
- [X] T048 [EDGE] Implement error handling for non-existent tasks in src/todo/cli.py
- [X] T049 [EDGE] Add user-friendly error messages for all error conditions in src/todo/cli.py

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T050 [P] Documentation updates in README.md
- [X] T051 Code cleanup and refactoring
- [X] T052 Performance optimization for handling up to 1000 tasks
- [X] T053 [P] Additional unit tests in tests/unit/ to achieve 90%+ coverage
- [X] T054 Security hardening
- [X] T055 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Edge Cases (Phase 8)**: Depends on all user stories being implemented
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

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
Task: "Unit test for Task creation with required fields in tests/unit/test_task.py"
Task: "Unit test for TodoList.add_task() in tests/unit/test_todo_list.py"
Task: "Integration test for CLI add command in tests/integration/test_cli.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task dataclass validation for non-empty title in src/todo/task.py"
Task: "Implement TodoList.add_task() method with ID assignment in src/todo/todo_list.py"
Task: "Implement CLI add command handler in src/todo/cli.py"
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