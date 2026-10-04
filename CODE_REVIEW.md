# Week 4 - Code Review and Refactoring Report

## Objective
Review an existing Student Management System, identify code smells and refactor it for clarity, performance, maintainability and testability.

## Issues Found
1. Long functions with multiple responsibilities.
2. Repeated database connection logic.
3. Inconsistent naming.
4. Limited input validation.
5. Database logic mixed with routes.
6. Repeated error handling.
7. Limited documentation.
8. Hard-coded configuration.

## Refactoring Implemented
- Separated database access into `database/database.py`.
- Moved business logic into `services/student_service.py`.
- Added centralized validation.
- Used meaningful function and variable names.
- Used parameterized SQL queries.
- Added unit tests.
- Added README and documentation.

## Before vs After
| Area | Before | After |
|---|---|---|
| Structure | Large/mixed functions | Modular layers |
| Database | Mixed with routes | Separate module |
| Validation | Repeated/limited | Centralized |
| Testing | Difficult | Easier |
| Maintainability | Low | Higher |
| Documentation | Limited | Improved |

## Testing
Add, view, update, delete, search, invalid email, empty input and duplicate roll-number scenarios were considered. Unit tests can be run using `python -m unittest discover -s tests -v`.

## Conclusion
The refactoring improved readability, maintainability, reliability and testability while preserving the core functionality of the Student Management System.
