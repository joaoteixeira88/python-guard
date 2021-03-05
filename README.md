# Python Guard

Guard is a fluent argument validation library that is intuitive, fast and extensible.


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

