---
id: 2
title: Update Todo Constitution
stage: constitution
date: 2026-01-05
surface: agent
model: Qwen
feature: none
branch: 001-todo-cli-app
user: dell
command: /sp.constitution
labels: [constitution, todo, spec-driven]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution Create or update the project constitution for a progressive, multi-phase in-memory-to-full-featured Todo application developed strictly via Spec-Driven Development using Qwen CLI + Spec-Kit Plus. This constitution applies to the entire project lifecycle from Phase I (basic console app) through potential future phases (intermediate organization features and advanced intelligent capabilities).

Immutable core principles (must never be violated):

1. Development Process
   - Strictly no manual coding — all implementation must be generated via Qwen CLI guided by specifications, plans, and tasks created through Spec-Kit Plus slash commands.
   - Follow the sequence: constitution → specify → clarify → plan → tasks → implement → review → commit.
   - All specifications, plans, and code generations must be versioned in the specs history folder.
   - Every phase/feature addition must have its own specification document.

2. Code Quality & Style (all phases)
   - Python 3.13+ with UV package management
   - Strict PEP 8 + modern Python style (black/ruff compatible)
   - Full type hints everywhere (use typing & dataclasses where appropriate)
   - Comprehensive docstrings (Google or NumPy style) on every public module/class/function
   - Separation of concerns: clear modular structure (data models, business logic, presentation/CLI, persistence when introduced)
   - Meaningful names, small functions (<30 lines ideal), early returns, single responsibility

3. Testing Standards (mandatory from Phase I)
   - pytest coverage ≥ 90% for all implemented features
   - Unit tests for core operations + edge cases (empty list, invalid IDs, max values, etc.)
   - Tests must be generated and kept in /tests/ folder

4. Error Handling & UX
   - Graceful, user-friendly error messages for all invalid inputs
   - Clear feedback after every operation
   - Consistent CLI interface style across all phases (subcommands preferred: add, list, update, delete, complete, etc.)

5. Phase-based Evolution Rules
   - Phase I (Basic): In-memory only, 5 core features (add, delete, update, view, mark complete/incomplete)
     → No persistence, no extra fields beyond id/title/description/completed
   - Intermediate Phase: Add organization & usability features (priorities, tags/categories, search/filter, sort)
     → Introduce additional task fields only when the phase specification explicitly requires them
     → Still prefer in-memory unless persistence is explicitly specified
   - Advanced Phase: Intelligent features (recurring tasks, due dates/reminders, notifications)
     → May introduce persistence (file/json/sqlite), scheduling concepts, external integrations only if explicitly specced
     → Must maintain backward compatibility with previous phases where reasonable

6. Non-functional Requirements (apply across all phases)
   - Simplicity first — avoid over-engineering for current phase
   - Performance: efficient operations up to at least 1000 tasks (O(1) lookups where possible)
   - Extensibility: design decisions should allow reasonable future extension without major refactoring
   - Documentation: always maintain up-to-date README.md with current features, usage examples, and phase status

7. Governance & Decision Rules
   - When in doubt, choose the simplest solution that satisfies the current phase specification
   - Never add features from later phases unless a new specification explicitly requests them
   - All AI-generated code must follow these principles — if conflict arises, report it and ask for clarification
   - Project name reference: "Progressive Todo" or "Todo Evolution"

Generate the constitution.md file containing these principles in clear, well-organized markdown format with numbered sections for easy reference by subsequent agents.
```

## Response snapshot

Updated the project constitution to reflect the progressive, multi-phase Todo application requirements. The new constitution includes 6 core principles covering development process, code quality, testing standards, error handling, phase-based evolution rules, and non-functional requirements. The constitution enforces spec-driven development with Qwen CLI, mandates no manual coding, and establishes clear phase-based evolution rules for the application from basic in-memory implementation to advanced features. Version updated from 1.0.0 to 2.0.0 to reflect the significant changes in project direction and governance.

## Outcome

- ✅ Impact: Constitution updated to reflect progressive multi-phase approach
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: Build Specification handoff available
- 🧠 Reflection: Constitution now properly guides multi-phase development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A