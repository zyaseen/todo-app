---
id: 1
title: Plan Advanced Features
stage: plan
date: 2026-01-05
surface: agent
model: Qwen
feature: 003-todo-advanced-features
branch: 003-todo-advanced-features
user: dell
command: /sp.plan
labels: [planning, todo, advanced]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/003-todo-advanced-features/plan.md
 - specs/003-todo-advanced-features/research.md
 - specs/003-todo-advanced-features/data-model.md
 - specs/003-todo-advanced-features/quickstart.md
 - specs/003-todo-advanced-features/contracts/cli-contract.md
tests:
 - none
---

## Prompt

```
/sp.plan Create a detailed, step-by-step technical implementation plan for adding ONLY the Advanced Level intelligent features to the existing Progressive Todo console application.

Current state (after Intermediate completion):
- Python 3.13+, UV managed, in-memory storage (list/dict of Task objects)
- Task model includes: id (int), title (str), description (str), completed (bool), priority (Optional[str]), tags (list[str])
- CLI commands exist: add, list (with search/filter/sort), update, delete, complete/toggle
- Modular structure: src/todo/ with task.py, todo_list.py (or similar), cli.py, main.py/__main__.py
- Clean code, type hints, docstrings, pytest tests for prior features

New requirements for Advanced Level — implement ONLY these two major feature groups:

1. Due Dates & Time Reminders
   - Add optional due_datetime: Optional[datetime.datetime] to Task
   - Support setting due date/time when adding/updating → Accept formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, relative like "tomorrow 3pm", "next friday", "in 2 days" (simple parsing)
   - Display in list: e.g. "due 2026-01-15 14:30" or "due tomorrow" + overdue warning (red/★ if past due)
   - Implement basic reminder system: When user runs app (or new "check-reminders"), show overdue + due-soon (next 24h) tasks
   - Optional: Desktop notification using plyer if user runs background checker
   - CLI extensions: add/update: --due "2026-01-20 15:00" or --due "tomorrow 9am"; list: --overdue, --due-soon (next 24h), --due-today; New command: reminders (or check-reminders) — shows urgent items with notification option

2. Recurring Tasks
   - Add optional recurrence: Optional[dict] to Task with pattern info → Supported: daily, weekly (on weekday), monthly (on day), yearly → Optional: end_date or count
   - When recurring task marked complete: Do NOT delete - create next instance with updated due_date according to pattern - Keep original as "template"
   - Display: recurring icon/symbol + next occurrence
   - CLI extensions: add/update: --recurring daily / --recurring weekly:friday / --recurring monthly:15 - New flag: --show-recurring (show template + next instances) - Rule: Only generate next when current completed (not auto-create in advance)

Technical & Design Guidelines (must follow):
- Update Task model: due_datetime: Optional[datetime.datetime], recurrence: Optional[dict]
- Keep in-memory approach (design for future migration)
- Use python-dateutil/dateparser for flexible parsing (if allowed; else simple parsing)
- For notifications: use plyer library
- Background checking: optional --watch mode that checks every X mins
- Never delete recurring templates — manage instances carefully
- UX: Clear visual distinction for overdue/due-soon/recurring, helpful error messages, confirmation when creating next recurring instance

Non-goals: Full calendar integration, mobile push notifications, email/SMS, complex NLP, cloud sync, GUI

Deliver detailed plan with: High-level changes, step-by-step sequence, file-by-file deltas, key decisions, new tests, risks.
```

## Response snapshot

Created a comprehensive implementation plan for the Advanced Level features of the Progressive Todo application. The plan includes:

1. Detailed technical context with language, dependencies, and performance goals
2. Complete constitution check ensuring alignment with all project principles
3. Clear project structure outlining all files to be modified or created
4. Research summary documenting key technical decisions:
   - Date parsing library choice (dateparser)
   - Recurring task implementation approach
   - Notification system (plyer)
   - Timezone handling (local system time)
   - Recurrence information storage
5. Extended data model specification with new fields (due_datetime, recurrence) and validation rules
6. Quickstart guide with examples for all new functionality
7. API contract documenting extended CLI commands and options
8. Proper update of agent context with new technologies (dateparser, plyer)

The plan maintains backward compatibility with existing functionality while extending the modular architecture to incorporate the new advanced features. All implementation will follow the existing code quality standards and testing practices.

## Outcome

- ✅ Impact: Complete technical implementation plan created with all required artifacts
- 🧪 Tests: none
- 📁 Files: specs/003-todo-advanced-features/plan.md, research.md, data-model.md, quickstart.md, contracts/cli-contract.md
- 🔁 Next prompts: Break the plan into tasks handoff available
- 🧠 Reflection: Plan aligns with all constitution principles and is ready for task breakdown

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A