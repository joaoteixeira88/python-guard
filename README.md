# Python Guard

Guard is a fluent argument validation library that is intuitive, fast and extensible.

## Description
“In computer programming, a guard is a boolean expression that must evaluate to true if the program execution is to 
continue in the branch in question. Regardless of which programming language is used, guard code or a guard clause 
is a check of integrity preconditions used to avoid errors during execution.” — Wikipedia

It typically does one (or any or all) of the following:
* Checks the passed-in parameters, and returns with an error if they're not suitable.
* Checks the state of the object, and bails out if the function call is inappropriate.
* Checks for trivial cases, and gets rid of them quickly.

This Guard project allows to add some validations to your method's parameters, such if it is null or not, 
is greater than a value,...


### Installing

To run this project, I advise to user virtualenv. The project requires python == 3.6.

```
mkvirtualenv -p $(which python3) pyguard
```

And

```
python setup.py install
```

### Usage

Here's some examples how to use this package:

```
from guard import Guard

Guard.NotNull(None) # Not Null Guard without parameter name and message
Guard.NotLessThan(-1, 0, "age") # Not Less Than Guard with parameter name and without custom message
Guard.NotAny([], "ags_lst", "This list must be at least one element.") # Not Any Guard with custom message
```


## Running the tests

```
pytest -v tests
```


## Authors

* **Joao Teixeira** - [joaoteixeira88](https://github.com/joaoteixeira88)

