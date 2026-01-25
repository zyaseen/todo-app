---
id: 1
title: Create Intermediate Features Plan
stage: plan
date: 2026-01-05
surface: agent
model: Qwen
feature: 002-todo-intermediate-features
branch: 002-todo-intermediate-features
user: dell
command: /sp.plan
labels: [planning, todo, intermediate]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-todo-intermediate-features/plan.md
 - specs/002-todo-intermediate-features/research.md
 - specs/002-todo-intermediate-features/data-model.md
 - specs/002-todo-intermediate-features/quickstart.md
 - specs/002-todo-intermediate-features/contracts/cli-contract.md
tests:
 - none
---

## Prompt

```
/sp.plan Create a detailed, step-by-step technical implementation plan for adding ONLY the Intermediate Level features to the existing Progressive Todo console application.

Current state (Phase I — already implemented):
- Python 3.13+, UV managed, in-memory storage (list or dict of Task objects)
- Task model: id (int), title (str), description (str), completed (bool)
- CLI commands exist: add, list/view, update, delete, complete/toggle
- Modular structure: src/todo/ with task.py, todo_list.py/manager, cli.py, main.py/__main__.py
- Clean code, type hints, docstrings, pytest tests covering basic features

Intermediate Level goals to implement (exactly these four feature groups):

1. Priorities
   - Add optional priority field to Task: Optional[str] with allowed values: "high", "medium", "low" or None
   - Support setting priority during add and update
   - Show in list view (e.g. [H], [M], [L] or simple emoji: 🔥/•/↓)

2. Tags/Categories
   - Add tags: list[str] to Task (default empty list)
   - Support adding multiple tags (comma-separated input) during add/update
   - Allow removing individual tags or clearing all during update
   - Display in list view (compact: #work #urgent)

3. Search & Filter
   - Add search: keyword matching in title OR description (case-insensitive, contains)
   - Add filters:
     - status: all / incomplete / completed
     - priority: high / medium / low / none
     - tag: contains specific tag
   - Support combining filters/search in list command

4. Sort
   - Add sort options for list output:
     - created (newest/oldest) — default
     - title (alphabetical)
     - priority (high > medium > low > none)
     - tag count (most → least)
   - Make sort selectable via flag/argument

Technical constraints & guidelines to follow:
- Keep everything in-memory (no persistence yet)
- Extend existing Task dataclass/class with new fields
- Do NOT break existing CLI commands — extend them elegantly
  Suggested CLI extensions (use argparse subcommands/flags):
  - add: --priority {high,medium,low} --tags "work,urgent,shopping"
  - update <id>: --priority ... --tags ... --add-tag ... --remove-tag ...
  - list: --search "keyword" --status incomplete --priority high --tag work --sort priority
- Prefer simple, readable solutions over complex abstractions
- Keep output clean & compact (use formatting like: "1 [H] #work Buy milk   [ ]")
- Add input validation (invalid priority → error message)
- Maintain clean architecture: put filtering/sorting/search logic in TodoManager class
- Update README.md with new command examples
- Add new pytest cases covering:
  - new fields persistence in memory
  - priority/tag validation
  - search matching (partial, case-insensitive)
  - filter combinations
  - all sort orders & directions

Plan structure requirements:
- High-level overview: what changes to existing files
- Step-by-step implementation sequence (recommended order of work)
- File-by-file changes (what to add/modify in task.py, todo_list.py, cli.py, etc.)
- Key architectural decisions (how to handle filtering/sorting efficiently)
- List of new/updated tests needed
- Any new dependencies? (should be none — use only stdlib)
- Estimated complexity & risk points

This plan should be incremental, safe to apply on top of the existing basic implementation, and ready to be broken down into concrete tasks via /sp.tasks.
Focus on clarity, pragmatism, and minimal disruption to existing code.
```

## Response snapshot

Completed the implementation planning for the intermediate features of the Todo application with:

1. Filled in the implementation plan with technical context, constitution check, and project structure
2. Created research.md documenting key decisions about task model extension, filtering/sorting implementation, CLI command extensions, tag storage, and priority representation
3. Created data-model.md defining the extended Task and TodoList entities with new fields, validation rules, and operations
4. Created quickstart.md with setup and usage instructions for the new features
5. Created contracts/cli-contract.md defining the extended command structure and API contracts
6. Updated the agent context with the new technology stack information

The plan extends the existing basic functionality while maintaining backward compatibility and following the same modular architecture.

## Outcome

- ✅ Impact: Complete implementation plan created with all required artifacts
- 🧪 Tests: none
- 📁 Files: specs/002-todo-intermediate-features/plan.md, research.md, data-model.md, quickstart.md, contracts/cli-contract.md
- 🔁 Next prompts: Create Tasks handoff available
- 🧠 Reflection: Planning phase completed successfully with all required artifacts

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A