<!-- 
Sync Impact Report:
- Version change: N/A → 2.0.0
- Modified principles: All principles updated to reflect progressive, multi-phase approach
- Added sections: Phase-based Evolution Rules, Development Process, Non-functional Requirements
- Removed sections: N/A
- Templates requiring updates: ✅ Updated
- Follow-up TODOs: None
-->
# Progressive Todo Constitution

## Core Principles

### I. Development Process (NON-NEGOTIABLE)
Strictly no manual coding — all implementation must be generated via Qwen CLI guided by specifications, plans, and tasks created through Spec-Kit Plus slash commands; Follow the sequence: constitution → specify → clarify → plan → tasks → implement → review → commit; All specifications, plans, and code generations must be versioned in the specs history folder; Every phase/feature addition must have its own specification document.

### II. Code Quality & Style Standards (NON-NEGOTIABLE)
Python 3.13+ with UV package management; Strict PEP 8 + modern Python style (black/ruff compatible); Full type hints everywhere (use typing & dataclasses where appropriate); Comprehensive docstrings (Google or NumPy style) on every public module/class/function; Separation of concerns: clear modular structure (data models, business logic, presentation/CLI, persistence when introduced); Meaningful names, small functions (<30 lines ideal), early returns, single responsibility.

### III. Testing Standards (NON-NEGOTIABLE)
pytest coverage ≥ 90% for all implemented features; Unit tests for core operations + edge cases (empty list, invalid IDs, max values, etc.); Tests must be generated and kept in /tests/ folder; Tests must verify both expected behavior and error conditions.

### IV. Error Handling & UX Consistency
Implement robust error handling for all user inputs; Validate command-line arguments and provide helpful error messages; Handle edge cases gracefully without crashing the application; Ensure the application fails safely when encountering unexpected conditions; Provide clear, helpful feedback for all user actions; Maintain consistent CLI interface style across all phases (subcommands preferred: add, list, update, delete, complete, etc.).

### V. Phase-based Evolution Rules
Phase I (Basic): In-memory only, 5 core features (add, delete, update, view, mark complete/incomplete) → No persistence, no extra fields beyond id/title/description/completed; Intermediate Phase: Add organization & usability features (priorities, tags/categories, search/filter, sort) → Introduce additional task fields only when the phase specification explicitly requires them → Still prefer in-memory unless persistence is explicitly specified; Advanced Phase: Intelligent features (recurring tasks, due dates/reminders, notifications) → May introduce persistence (file/json/sqlite), scheduling concepts, external integrations only if explicitly specced → Must maintain backward compatibility with previous phases where reasonable.

### VI. Non-functional Requirements
Simplicity first — avoid over-engineering for current phase; Performance: efficient operations up to at least 1000 tasks (O(1) lookups where possible); Extensibility: design decisions should allow reasonable future extension without major refactoring; Documentation: always maintain up-to-date README.md with current features, usage examples, and phase status.

## Additional Constraints

Technology stack requirements:
- Python 3.13+ as the primary runtime
- UV for package management
- Argparse for command-line parsing
- Rich for formatted output
- Pytest for testing framework
- No external dependencies beyond the specified stack

Project structure requirements:
- `/src` directory for all source code
- `/specs` directory for versioned specifications
- `/tests` directory for all test files
- `README.md` with setup instructions

## Development Workflow

All development must follow spec-driven iterations via Qwen CLI; No manual coding without prior specification; Each feature must have clear acceptance criteria before implementation; Code reviews must verify compliance with all constitution principles; Maintain proper git practices with descriptive commit messages; When in doubt, choose the simplest solution that satisfies the current phase specification; Never add features from later phases unless a new specification explicitly requests them; All AI-generated code must follow these principles — if conflict arises, report it and ask for clarification.

## Governance

This constitution supersedes all other development practices; Amendments require explicit documentation and approval; All decisions must prioritize simplicity and avoid over-engineering; The AI agent must implement only required features as specified in the current phase; Project name reference: "Progressive Todo" or "Todo Evolution"; Spec-Kit Plus must be used for all project management.

**Version**: 2.0.0 | **Ratified**: 2026-01-05 | **Last Amended**: 2026-01-05