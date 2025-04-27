# Python vs TypeScript/JavaScript: A Beginner-Friendly `Data Types` Comparison

![Data Types](./public/datatype.png)

| Python 🐍                    | TypeScript/JavaScript 🟦|
| ---------------------------- | -----------------------------|
## ***STRING***

| `name: str = "Ali"`          | `let name: string = "Ali";`|


#### String Interpolation

```python
first_name = "Fahad"
last_name = "Khan"
full_name = f"{first_name} {last_name}"
```

 ***Comparison with JavaScript/TypeScript:***

```ts
let firstName = "Fahad";
let lastName = "Khan";
let fullName = `${firstName} ${lastName}`; // Template literals
```

- Python uses `f"{variable}"`, while JavaScript/TypeScript uses **template literals** `${variable}`.

---

- #### String Formatting

```python
greeting = "Hello, {}!".format(first_name)
```

 ***Comparison with JavaScript/TypeScript:***

- Not available in JavaScript/TypeScript

---

- #### Old-Style Formatting

```python
greeting = "Hello, %s!" % first_name
```
**Another example using `%` operator:**

```python
name: str = 'John'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000  # 70.536000

my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight is %2f Kg.''' % (name, first_letter, age, my_weight)
print(my_string)
```
- `%s` → string
- `%d` → integer
- `%f` → float
- `%.2f` → float with 2 decimal places
- `%x` → hexadecimal (lowercase)
- `%X` → hexadecimal (uppercase)
- `%o` → octal
- `%e` → scientific notation (lowercase)
- `%E` → scientific notation (uppercase)
- `%c` → character (based on integer value)
- `%p` → pointer address

 ***Comparison with JavaScript/TypeScript:***

- Not available in JavaScript/TypeScript

---

- #### String Concatenation

```python
greeting = "Hello, " + first_name + "!"
```

 ***Comparison with JavaScript/TypeScript:***

```ts
let greeting = "Hello, " + firstName + "!";
```

- Both Python and JavaScript/TypeScript use the `+` operator for string concatenation.

---

- #### Joining Strings from Arrays

```python
my = "John"
x = "#".join(my)
print(x)  # #J#o#h#n
```
The join() method takes all items in an iterable and joins them into one string.


 ***Comparison with JavaScript/TypeScript:***

```ts
let arr = ["Hello, ", "Fahad", "!"];
let greeting = arr.join(""); // Join array elements
```

- In both Python and JavaScript/TypeScript, `.join()` is used to join elements from an iterable (list/array) into a single string.

---

## String Methods

#### Convert to Uppercase

```python
print(full_name.upper())
```

```ts
console.log(fullName.toUpperCase());
```

#### Convert to Lowercase

```python
print(full_name.lower())
```

```ts
console.log(fullName.toLowerCase());
```

#### casefold()

- Also converts string into lowercase. `.casefold()` is more aggressive than `.lower()` (e.g., it handles "ß" to "ss").

```python
a = "Straße"
b = "strasse"
print(a.lower())   # Output: "straße"
print(a.casefold()) # Output: "strasse"
```

---



#### Trim Whitespace

```python
print(full_name.strip())
```

```ts
console.log(fullName.trim());
```

#### Replace Substrings

```python
text = "quick brown fox"
print(text.replace("fox", "dog"))
```
In python `.replace()` works globally by default.
```ts
let text = "quick brown fox";
console.log(text.replace("fox", "dog"));
```
In ts/js it replaces only the first match..

#### Title Case (First Letter Capitalized)

```python
print("hello world".title())
```

```ts
// No built-in method, need custom function
console.log("hello world".replace(/\b\w/g, (c) => c.toUpperCase()));
```

#### capitalize()

- Converts only the first character to uppercase.

```python
txt = "hello, and welcome to my world."
print(txt.capitalize())  # Output: "Hello, and welcome to my world."
```

---



#### Swap Case (Upper to Lower & Vice Versa)

```python
print("Hello PYTHON".swapcase())
```

- **Not available in JavaScript/TypeScript**

#### Check if String is Digit/Alpha/Alphanumeric

```python
print("12345".isdigit())  # True
print("Hello".isalpha())  # True
print("Hello123".isalnum())  # True
```

```ts
console.log(/^[0-9]+$/.test("12345")); // True
console.log(/^[a-zA-Z]+$/.test("Hello")); // True
console.log(/^[a-zA-Z0-9]+$/.test("Hello123")); // True
```

#### Find Substring Index

```python
print("quick brown fox".find("fox"))  # Returns index
print("quick brown fox".find("dog"))  # Returns -1 (not found)
```

```ts
console.log("quick brown fox".indexOf("fox"));
// return index
console.log("quick brown fox".indexOf("dog"));
// return -1 if not found
```

#### Count Occurrences

```python
print("quick brown fox".count("o")) #2
```

- **Not available in JavaScript/TypeScript (requires regex or loop)**

#### String Slicing

```python
name = "Hamza Ahmed Alvi"
print(name[0:5])  # Hamza
print(name[:5])   # Hamza
print(name[2:])   # mza Ahmed Alvi
```

```ts
let name = "Hamza Ahmed Alvi";
console.log(name.substring(0, 5)); // Hamza
console.log(name.substring(2)); // mza Ahmed Alvi
```


---

- **Python:** slicing syntax → `obj[start:end:step]`  
- **JS/TS:** use `slice(start, end)` or `substring(start, end)` (no `step`)  
- In `py/ts/js`, slice[] and range() never include the second argument.
- Use negative indexes to slice from the end of the string.
- The 3rd parameter as -1 will reverse the slice.
- **Step** (Python only):  
  - `2` → skip every 2nd item / n no.of items   
  - `-1` → reverse  

Use `[::-1]` for full reverse in Python.


#### center()

- Centers the string. First parameter: total length, second parameter: padding character.

```python
txt = "banana"
print(txt.center(20))     # Output: "       banana"
print(txt.center(20, '>')) # Output: ">>>>>>>banana>>>>>>>"
```

---

#### format()

- Replaces `{}` with values. Supports string interpolation with format specifiers.

```python
txt = "We have {:<8} chickens."
print(txt.format(49)) # Output: "We have 49       chickens."
```

###### Alignment Options:

- `:<` Left aligns.
- `:>` Right aligns.
- `:^` Centers.

###### Sign Handling:

- `:=` Places the sign at the left.
- `:+` Adds a plus sign for positive values.
- `:-` Adds a minus sign only for negative values.
- `:` Adds space before positive numbers.

###### Number Formatting:

- `:,` Comma separator for thousands.
- `:_` Underscore separator for thousands.
- `:b` Binary format.
- `:c` Unicode character.
- `:d` Decimal format.
- `:e` Scientific notation (lowercase).
- `:E` Scientific notation (uppercase).
- `:ⁿf` Fixed-point format, where `ⁿ` is no.digits
- `:o` Octal format.
- `:x` Hex format (lowercase).
- `:X` Hex format (uppercase).
- `:%` Percentage format.

---

#### ljust()

- Left-aligns a string within a specified width, padding with spaces (or a specified character).

```python
text = "Hello"
result = text.ljust(10, '-')
print(result)  # Output: "Hello-----"
```

---

#### lstrip()

- Returns a version of the string with leading spaces removed.

```python
txt = "   Hello"
print(txt.lstrip())  # Output: "Hello"
```

---

#### maketrans()

- Creates a translation table for string replacement, used with `translate()`.

```python
trans = str.maketrans("abc", "123")
text = "abc abc"
print(text.translate(trans))  # Output: "123 123"
```

###### Advanced Usage:

```python
trans = str.maketrans({"a": "1", "b": "2", "c": "3"})
text = "abc"
print(text.translate(trans))  # Output: "123"
```

---

#### splitlines()

- Splits a string at line breaks and returns a list.
- Note: `\n `breaks line when displaying, but not when processing. so we need splitlines()
```python
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())  # Output: ['Thank you for the music', 'Welcome to the jungle']
```

---

#### translate()

- Translates a string using a translation table or a dictionary.

```python
trans = str.maketrans("abc", "123")
text = "abc"
print(text.translate(trans))  # Output: "123"
```

#### **`encode()`**: Encodes the string.

#### **`endswith(suffix)`**: Checks if string ends with the given suffix.

#### **`expandtabs(tabsize)`**: Sets tab size.

#### **`format_map()`**: Formats specified values in the string.

#### **`index(substring)`**: Returns the position of the substring.

#### **`partition(separator)`**: Partitions the string into a tuple of three parts.

#### **`rfind(substring)`**: Finds the last occurrence of the substring.

#### **`rindex(substring)`**: Finds the last occurrence of the substring and returns its index.

#### **`rjust(width, char)`**: Right-aligns the string within the specified width, pads with `char`.

#### **`rpartition(separator)`**: Partitions the string into three parts from the right.

#### **`rsplit()`**: Splits the string at the specified separator, from the right.

#### **`rstrip()`**: Removes trailing whitespaces.

#### **`split()`**: Splits the string at the specified separator.

#### **`startswith(prefix)`**: Checks if the string starts with the specified prefix.

#### **`zfill(width)`**: Pads the string with zeros on the left to the specified width.

#### **`isascii()`**: Checks if all characters are ASCII.

#### **`isdecimal()`**: Checks if all characters are decimals.

#### **`isidentifier()`**: Checks if the string is a valid identifier.

#### **`islower()`**: Checks if all characters are lowercase.

#### **`isnumeric()`**: Checks if all characters are numeric.

#### **`isprintable()`**: Checks if all characters are printable.

#### **`isspace()`**: Checks if all characters are whitespaces.

#### **`istitle()`**: Checks if the string follows title case.

#### **`isupper()`**: Checks if all characters are uppercase.

#### **`len()`**

```py
a = "Hello, World!"
print(len(a))
```

#### **`in/not in`** Check if "free" is present in the following text:
```py
txt = "The best things in life are free!"
print("free" in txt)
```
---

#### Docstring (Multiline Comments)

```python
"""
This is a docstring.
Used for documentation.
"""
```

```ts
/*
This is a multiline comment.
Used for documentation.
*/
```

- Python uses `"""Triple Quotes"""`, while JavaScript/TypeScript uses `/* Block Comments */`.
---
- Triple quotes (""") let you write multi-line strings, so instead of using \n to break lines, you can just write the text across lines.
* ```py
  print("""
  Line 1    
  Line 2
  Line 3
  """)
  ```
    same as
- ```py
  print("Line 1\nLine 2\nLine 3")
  ```

---


## ***INTEGER***

| `x: int = 10`                | `let x: number = 10;`|

## ***FLOAT***

| `y: float = 3.14`            | `let y: number = 3.14;`|

## ***COMPLEX***


## ***LIST vs Array***

Python uses **lists**, while TypeScript/JavaScript uses **arrays**.

```python
nums: int[] = [1, 2, 3]  # List
```

```typescript
let nums: number[] = [1, 2, 3]; // Array
```

## ***Tuples vs Arrays (Readonly)***

- Python has **tuples** (immutable), while TypeScript has **readonly arrays or tuples**.

```python
data = (4, 5, 6)  # Tuple
```

```ts
const data: readonly [number, number, number] = [4, 5, 6];
```

---

## ***RANGE***

## ***Dictionaries vs Objects***
Python uses **dict**, while TypeScript/JavaScript uses **objects or Map**.

```python
info = {"name": "Ali", "age": 25}  # Dictionary
```

```ts
const info: { name: string; age: number } = { name: "Ali", age: 25 };
```

## ***SET***

```python
unique = {1, 2, 3}  # Set
```

```ts
const unique = new Set([1, 2, 3]); // Set
```
**Set in Python**  
- `set`: `{}` — removes duplicates (list `[]` doesn't).
- **Set** is used to create a **unique list**.
- `{}` alone is an **empty dict**, **not** an empty set.  
  (Empty set = `set()`)
- **Sets are unordered** — we can't predict the sequence.
- **Hashing** happens on **each item**, not on the whole set.


## ***FROZEN SET***

## ***BOOL***

| `is_true: bool = True`       | `let isTrue: boolean = true;`|

## ***BYTE***

Bytes & Bytearray vs Buffer

- Python has **bytes & bytearray**, while JavaScript has **Buffer**.

```python
b = b"hello"  # Bytes
ba = bytearray(b)  # Mutable Bytearray
```

```ts
const b = Buffer.from("hello"); // Buffer
```

## ***BYTE ARRAY***

## ***MEMORY VIEW***

## ***NONE***

| `x: None = None` (null equivalent) | `let x: null = null;`|

---

### Key Differences

- **Python lists ≈ JavaScript/TypeScript arrays**
- **Python tuples ≈ TypeScript readonly arrays**
- **Python dict ≈ JavaScript objects/Map**
- **Python has `None`, JavaScript has `null/undefined`**
- **Python uses indentation and colons ":" for blocks, TypeScript uses `{}`**
- Python is **dynamically typed**, while TypeScript is **statically typed**. 🚀

---