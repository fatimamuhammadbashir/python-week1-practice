
Python Week 1 Practice

This repository contains my Week 1 Python practice exercises. The exercises demonstrate the core Python concepts I learned and practiced during Week 1.

Concepts Covered

1. Variables and Data Types
2. Conditionals
3. Loops
4. Functions
5. Modules
6. Error Handling
7. File Handling
8. Script Organisation

Automated Tests

This repository includes automated tests for:

- Exercise 4 — Functions
- Exercise 5 — Modules

The tests are run automatically using GitHub Actions.

Project Structure

python-week1-practice/
├── exercise1_variables_data_types/
├── exercise2_conditionals/
├── exercise3_loops/
├── exercise4_functions/
│   ├── functions.py
│   └── test_functions.py
├── exercise5_modules/
│   ├── mytools.py
│   ├── main.py
│   └── test_mytools.py
├── exercise6_error_handling/
├── exercise7_file_handling/
├── exercise8_script_organisation/
└── README.md

How to Run

Each exercise contains Python files that can be run with Python 3.

Example:

python exercise4_functions/functions.py

To run the automated tests:

pytest

GitHub Actions

GitHub Actions is configured to automatically test the Python project whenever changes are pushed to the "main" branch.

The latest workflow run completed successfully
