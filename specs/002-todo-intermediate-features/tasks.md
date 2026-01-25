---

description: "Task list for Todo Intermediate Features"
---

# Tasks: Todo Intermediate Features

**Input**: Design documents from `/specs/002-todo-intermediate-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are required for all new intermediate features and edge cases per the specification.

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

- [X] T001 Update existing Task dataclass in src/todo/task.py with priority and tags fields
- [X] T002 [P] Update TodoList class in src/todo/todo_list.py with new filtering/sorting/search methods
- [X] T003 [P] Update CLI argument parser in src/todo/cli.py with new command options

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Extend Task dataclass validation for priority values in src/todo/task.py
- [X] T005 Implement tag parsing and validation in src/todo/task.py
- [X] T006 [P] Implement search_tasks method in src/todo/todo_list.py
- [X] T007 [P] Implement filter_tasks method in src/todo/todo_list.py
- [X] T008 [P] Implement sort_tasks method in src/todo/todo_list.py
- [X] T009 Implement combine_filters_search method in src/todo/todo_list.py
- [X] T010 Update add_task method to accept priority and tags in src/todo/todo_list.py
- [X] T011 Update update_task method to handle priority and tags in src/todo/todo_list.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task with Priority and Tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with priority levels and tags so that they can better organize and categorize their tasks.

**Independent Test**: The application allows users to add a new task with title, description, priority level (high/medium/low/none), and tags (comma-separated list), assigns it a unique ID, and displays a confirmation message. The task appears in the list with the specified priority and tags.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T012 [P] [US1] Unit test for Task creation with priority and tags in tests/unit/test_task.py
- [X] T013 [P] [US1] Unit test for TodoList.add_task() with priority and tags in tests/unit/test_todo_list.py
- [X] T014 [P] [US1] Integration test for CLI add command with priority and tags in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Extend CLI add command to accept --priority flag in src/todo/cli.py
- [X] T016 [P] [US1] Extend CLI add command to accept --tags flag in src/todo/cli.py
- [X] T017 [US1] Update CLI add command handler to process priority and tags in src/todo/cli.py
- [X] T018 [US1] Add input validation for priority values in src/todo/cli.py
- [X] T019 [US1] Add input validation for tags format in src/todo/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List Tasks with Filtering and Sorting (Priority: P1)

**Goal**: Enable users to filter and sort their tasks so that they can focus on the most important or relevant ones.

**Independent Test**: The application displays filtered and sorted tasks with their ID, title, description (or "No description"), priority indicator, tags, and status indicator ([ ] for incomplete, [x] for complete).

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T020 [P] [US2] Unit test for TodoList.filter_tasks() by status in tests/unit/test_todo_list.py
- [X] T021 [P] [US2] Unit test for TodoList.filter_tasks() by priority in tests/unit/test_todo_list.py
- [X] T022 [P] [US2] Unit test for TodoList.filter_tasks() by tag in tests/unit/test_todo_list.py
- [X] T023 [P] [US2] Unit test for TodoList.sort_tasks() by various criteria in tests/unit/test_todo_list.py
- [X] T024 [P] [US2] Integration test for CLI list command with filters and sorting in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T025 [P] [US2] Extend CLI list command to accept --status flag in src/todo/cli.py
- [X] T026 [P] [US2] Extend CLI list command to accept --priority flag in src/todo/cli.py
- [X] T027 [P] [US2] Extend CLI list command to accept --tag flag in src/todo/cli.py
- [X] T028 [P] [US2] Extend CLI list command to accept --sort flag in src/todo/cli.py
- [X] T029 [P] [US2] Extend CLI list command to accept --reverse flag in src/todo/cli.py
- [X] T030 [US2] Update CLI list command handler to apply filters and sorting in src/todo/cli.py
- [X] T031 [US2] Update task display format to show priority and tags in src/todo/cli.py
- [X] T032 [US2] Add message when no tasks match filters in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Priority and Tags (Priority: P2)

**Goal**: Enable users to update the priority and tags of existing tasks so that they can adjust their importance and categorization as needed.

**Independent Test**: The application allows users to update the priority and/or tags of an existing task by ID, changing these attributes, and confirms the update.

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T033 [P] [US3] Unit test for TodoList.update_task() with priority and tags in tests/unit/test_todo_list.py
- [X] T034 [P] [US3] Unit test for tag manipulation (add/remove) in tests/unit/test_todo_list.py
- [X] T035 [P] [US3] Integration test for CLI update command with priority and tags in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T036 [P] [US3] Extend CLI update command to accept --priority flag in src/todo/cli.py
- [X] T037 [P] [US3] Extend CLI update command to accept --tags flag in src/todo/cli.py
- [X] T038 [P] [US3] Extend CLI update command to accept --add-tag flag in src/todo/cli.py
- [X] T039 [P] [US3] Extend CLI update command to accept --remove-tag flag in src/todo/cli.py
- [X] T040 [US3] Update CLI update command handler to process priority and tags in src/todo/cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Search Tasks by Keyword (Priority: P2)

**Goal**: Enable users to search for tasks by keyword so that they can quickly find specific tasks among many.

**Independent Test**: The application searches through task titles and descriptions for the specified keyword and displays matching tasks.

### Tests for User Story 4 (REQUIRED) ⚠️

- [X] T041 [P] [US4] Unit test for TodoList.search_tasks() functionality in tests/unit/test_todo_list.py
- [X] T042 [P] [US4] Integration test for CLI list command with --search flag in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T043 [P] [US4] Extend CLI list command to accept --search flag in src/todo/cli.py
- [X] T044 [US4] Update CLI list command handler to apply search filter in src/todo/cli.py
- [X] T045 [US4] Implement case-insensitive search in src/todo/todo_list.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Combined Filter Operations (Priority: P3)

**Goal**: Enable users to combine multiple filters (priority, status, tags, search) so that they can create complex queries to find exactly what they need.

**Independent Test**: The application applies multiple filters simultaneously and displays only tasks that match all specified criteria.

### Tests for User Story 5 (REQUIRED) ⚠️

- [X] T046 [P] [US5] Unit test for TodoList.combine_filters_search() with multiple criteria in tests/unit/test_todo_list.py
- [X] T047 [P] [US5] Integration test for CLI list command with combined filters in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T048 [P] [US5] Update CLI list command handler to combine all filters and search in src/todo/cli.py
- [X] T049 [US5] Ensure all filter options work together in src/todo/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Edge Cases & Error Handling

**Goal**: Handle all specified edge cases and error conditions

**Independent Test**: The application properly handles all edge cases and provides user-friendly error messages.

### Tests for Edge Cases (REQUIRED) ⚠️

- [X] T050 [P] [EDGE] Unit test for invalid priority value handling in tests/unit/test_todo_list.py
- [X] T051 [P] [EDGE] Unit test for empty search query handling in tests/unit/test_todo_list.py
- [X] T052 [P] [EDGE] Unit test for no-match filter scenarios in tests/unit/test_todo_list.py
- [X] T053 [P] [EDGE] Integration test for error conditions in tests/integration/test_cli.py

### Implementation for Edge Cases

- [X] T054 [P] [EDGE] Implement validation for priority values in src/todo/task.py
- [X] T055 [EDGE] Add error handling for invalid priority input in src/todo/cli.py
- [X] T056 [EDGE] Add appropriate messages when no tasks match filters in src/todo/cli.py
- [X] T057 [EDGE] Handle empty search queries appropriately in src/todo/cli.py

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T058 [P] Update README.md with new command examples
- [X] T059 Code cleanup and refactoring
- [X] T060 Performance optimization for filtering and sorting operations
- [X] T061 [P] Additional unit tests in tests/unit/ to achieve 90%+ coverage
- [X] T062 Security hardening
- [X] T063 Run quickstart.md validation

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
Task: "Unit test for Task creation with priority and tags in tests/unit/test_task.py"
Task: "Unit test for TodoList.add_task() with priority and tags in tests/unit/test_todo_list.py"
Task: "Integration test for CLI add command with priority and tags in tests/integration/test_cli.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Extend CLI add command to accept --priority flag in src/todo/cli.py"
Task: "Extend CLI add command to accept --tags flag in src/todo/cli.py"
Task: "Update CLI add command handler to process priority and tags in src/todo/cli.py"
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