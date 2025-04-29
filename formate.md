## Use the Slice Operator

You can make a copy of a list by using the `:` (slice) operator.

In Python, "guards" usually mean:

The second parameter in the `range()` function never reaches the specified value. To include that value, you can add it dynamically, like `1 + num`. This ensures the range includes the desired value, even if it's a variable.

For example:

```python
num = 10
for i in range(1, 1 + num, 3):
    print(i)  # Output: 1, 4, 7, 10
```

`\r` is a carriage return. It removes previous words and moves the cursor to the beginning of the line.

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
