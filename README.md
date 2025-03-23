# Python Guard

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)


## Overview

Python Guard is a fluent argument validation library that is intuitive, fast, and extensible.

## Description

> "In computer programming, a guard is a boolean expression that must evaluate to true if the program execution is to continue in the branch in question. Regardless of which programming language is used, guard code or a guard clause is a check of integrity preconditions used to avoid errors during execution." — *Wikipedia*

This library helps ensure method parameters meet specific conditions before execution. It typically does the following:

- Checks the passed-in parameters and raises an error if they are invalid.
- Validates the state of an object to prevent inappropriate function calls.
- Detects trivial cases and handles them efficiently.

## Installation

### Prerequisites

Ensure you have Python 3.6 or higher installed.

### Using Poetry (Recommended)

[Poetry](https://python-poetry.org/) is the recommended dependency management tool for this project.

```sh
# Install Poetry if not already installed
pip install poetry

# Clone the repository
git clone https://github.com/joaoteixeira88/python-guard.git
cd python-guard

# Install dependencies
poetry install
```

### Alternative: Using Virtualenv

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install .
```

## Usage

Here's how you can use Python Guard:

```python
from guard import Guard

Guard.NotNull(None)  # Ensures value is not null
Guard.NotLessThan(-1, 0, "age")  # Ensures value is not less than the given threshold
Guard.NotAny([], "items", "This list must have at least one element.")  # Ensures list is not empty
```

## Running Tests

To run the test suite, use:

```sh
pytest -v tests
```

If using Poetry:

```sh
poetry run pytest -v tests
```

## License

This project is licensed under the MIT License.

## Author

**João Teixeira** - [joaoteixeira88](https://github.com/joaoteixeira88)

