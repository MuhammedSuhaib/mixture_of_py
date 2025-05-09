
In Python, "guards" usually mean:  early checks to avoid wrong execution.

---

### List Properties

- **Ordered**: Lists are ordered, meaning that the items in the list have a specific order and can be accessed by their index.
- **Mutable**: Lists are mutable, meaning that they can be modified after they are created.
- **Indexed**: Lists are indexed, meaning that each item in the list has a specific index that can be used to access it.
- **Dynamic size**: Lists can grow or shrink dynamically as elements are added or removed.
- **Heterogeneous**: Lists can contain elements of different data types, such as integers, strings, floats, and other lists.
- **Supports duplicate values**: Lists can contain duplicate values.

Example:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[-3])  # Output: apple (accessing element in reverse order)
```

---

### Append vs Extend

- **`append`**: Adds a single value to the list.
- **`extend`**: Adds multiple elements to the list.

---

### `pop()` vs `remove()`

| Feature         | `pop()`                     | `remove()`                  |
|------------------|-----------------------------|-----------------------------|
| **Based on**     | Index                      | Value                      |
| **Return value** | Yes (removed item)         | No (returns `None`)        |
| **Error if...**  | Index out of range         | Value not found            |
| **Default use**  | Removes the last item if no index is given | Removes the first matching value |

Example:

```python
# Handling errors gracefully with pop()
try:
    item = my_list.pop(2)
except IndexError:
    item = "No such item found"
```

---

### Removing All Occurrences of a Value

You can't remove all occurrences of a value with a single `remove()` call. Use a loop or list comprehension instead.

**Loop Method**:

```python
lst = [1, 2, 1, 3]
while 1 in lst:
    lst.remove(1)
```

**List Comprehension Method**:

```python
lst = [x for x in lst if x != 1]
```

**Using `filter()`**:

```python
lst = list(filter(lambda x: x != 1, lst))
```

---

### Sorting Lists

- **Ascending Order**:

```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
```

- **Descending Order**:

```python
numbers.sort(reverse=True)
```

- **String Length (Shortest First)**:

```python
words.sort(key=len)
```

- **String Length (Longest First)**:

```python
words.sort(key=lambda word: len(word))
```

---

### List Comprehension

List comprehension is a concise way to create new lists by applying a transformation or filter to each element.

**Syntax**:

```python
new_list = [expression for element in iterable if condition]
```

Example:

```python
squared_numbers = [x**2 for x in range(10) if x % 2 == 0]
```

---

## Tuples

- **Hashable**: Tuples can be used as keys in dictionaries because they are immutable.
- **Allow duplicates**: Tuples allow duplicate values.

### Tuple Operations

- **Slicing**:

```python
tuple2 = (10, 20, 30)
print(tuple2[1:])  # Output: (20, 30)
```

- **Concatenation**:

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (10, 20, 30)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('apple', 'banana', 'cherry', 10, 20, 30)
```

- **Nesting**:

```python
nested_tuple = (tuple1, tuple2)
print(nested_tuple)  # Output: (('apple', 'banana', 'cherry'), (10, 20, 30))
```

- **Repeating**:

```python
tuple4 = tuple2 * 2
print(tuple4)  # Output: (10, 20, 30, 10, 20, 30)
```

- **Unpacking**:

```python
a, b, c = tuple1
print(a, b, c)  # Output: apple banana cherry
```

---

## Dictionaries

- **Unindexed**: Items are accessed using keys, not indices.
- **Unique keys**: Keys must be unique, but values can be duplicated.

### Accessing Items

```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car["model"])  # Output: Mustang
print(car.get("model"))  # Output: Mustang
```

### Adding/Modifying Items

```python
car["color"] = "red"
```

### Dictionary Comprehension

```python
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit = {str(c) + "C": str((c * 9/5) + 32) + "F" for c in celsius_temps}
```

---

## Sets

- **Unordered**: Elements have no specific order.
- **Unique**: No duplicate elements.
- **Mutable**: Can add or remove elements.

### Creating Sets

```python
my_set = {1, 2, 3, 4, 5}
my_set2 = set([123, 452, 5, 6])
```

### Set Operations

- **Union**:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
```

- **Difference Update**:

```python
my_set.difference_update({1, 3})
```

---

## Frozenset

- **Immutable**: Cannot be modified after creation.
- **Hashable**: Can be used as dictionary keys.

```python
my_frozenset = frozenset([1, 2, 3])
```

---

## Garbage Collection

Python automatically manages memory using garbage collection. You can manually trigger it:

```python
import gc
gc.collect()
```

---

## Modules

- **Built-in**: Pre-installed with Python.
- **User-defined**: Custom modules.
- **External**: Installed via `pip`.

### Import Styles

| Style                  | Bytecode Impact | Readability | Performance |
|------------------------|-----------------|-------------|-------------|
| `import module`        | ✅ Minimal      | ✅ Clear    | ✅ Fast     |
| `from module import *` | ❌ Bigger       | ❌ Confusing| ❌ Slower   |

---

## Functions

- **Global Scope**: Functions defined at the top level of a module are globally accessible.
- **Keyword Arguments**: Allow changing the order of arguments.

```python
def print_info(name, age=35):
    print(f"Name: {name}, Age: {age}")
```

---

## Generators

Generators are functions that yield values one at a time using `yield`.

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```
### Scenarios Where Exception Handling is Crucial
File Operations: Handling missing files or permission errors during file access.

User Input: Validating and handling invalid or unexpected input from users.

Network Operations: Managing connection errors or timeouts in network requests.

Mathematical Operations: Preventing division by zero or invalid calculations.

---
Quick walk-through:

### `try`, `except`, `else`, `finally`
- `try`: Code that might throw an error.
- `except`: Runs if an error happens in `try`.
- `else`: Runs if no error in `try`.
- `finally`: Always runs (error or not).

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error!")
except Exception:  # Catches anything not caught above
    print("An unexpected error occurred.")
else: #optional runs if no error in try block
    print("No error")
finally: #optional always runs
    print("Always runs")
```
---
cheatsheet for common exceptions:

```python
# Common exceptions
try:
    # risky code
except TypeError:
    print("Wrong type! Check your data.")
except ValueError:
    print("Bad value! Try again.")
except ZeroDivisionError:
    print("Can't divide by zero!")
except IndexError:
    print("Index out of range!")
except KeyError:
    print("Key not found in dict!")
except AttributeError:
    print("Object has no such attribute!")
except FileNotFoundError:
    print("File not found!")
except ImportError:
    print("Import failed!")
except NameError:
    print("Variable not defined!")
except RuntimeError:
    print("Something went wrong during execution!")
except PermissionError:
    print("You don’t have permission!")
except Exception:
    print("Something went wrong.")

#You create a new custom error by creating  classes for example (NegativeNumberError) that inherits from the base Exception class.like
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!

```
---
---

### `raise`
- Manually throw an error.
raise will stop the current flow of execution and look for an except block to handle the exception. If no except block catches the raised exception, the program will crash (terminate).

```python
raise ValueError("Invalid value")
```
You can use `raise` without a custom message by just raising the exception class itself:

### Example:

```python
raise ValueError  # Will raise a default ValueError
```

This will trigger the `ValueError` exception without any custom message. If uncaught, it will display something like:

```
ValueError
```

### Re-raising an existing exception without a custom message:

```python
try:
    # Some code
    raise ValueError("Something went wrong!")
except ValueError:
    raise  # Re-raises the same exception without modifying the message
```

This will re-raise the same `ValueError` and propagate it up the stack.
---
## Equivalent of throw and throws in Python
In Java, throw and throws are used for exception handling. Python doesn’t have a direct equivalent to throws, but throw is equivalent to Python's raise.



✔ Python doesn’t enforce throws, but you can document exceptions in docstrings or use type hints (NoReturn).

### `NoReturn` (from `typing`)
- Used to mark functions that **never return** (e.g., infinite loop or always raises error).

```python
from typing import NoReturn

def crash() -> NoReturn:
    raise RuntimeError("Crash!")
```

---

### Alternative: `None` or omit return type
- If unsure or return nothing, use `None` or omit type hint.

```python
def log(msg: str) -> None:
    print(msg)

# or just
def log(msg: str):
    print(msg)
```

Want a TS version of any part?
When Should You Stick to NoReturn?
If you are using type checking tools like mypy, NoReturn is still the best choice for functions that:

Always raise an exception

Never return (e.g., an infinite loop)

Terminate the program (sys.exit())

✅ But if you are not using static type checking, omitting the type hint or using None may be enough.
