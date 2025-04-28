<!-- default font size ==14 -->
### **1. Python String Prefixes & Formatting**
---
#### **String Prefixes:**
1. **`r""`** → **Raw String Literal**  
   - Escape sequences are not processed (`\n`, `\t`, etc.)
  
2. **`b""`** → **Byte String**  
   - Stores bytes, not characters.

3. **`f""`** → **Formatted String**  
   - Embed expressions with `{}`.
ing Formatting (for `format()` and f-strings):**
---

### **Escape Sequences:**

- `\'` → Single Quote  
- `\\` → Backslash  
- `\n` → New Line  
- `\r` → Carriage Return  
- `\t` → Tab  
- `\b` → Backspace  
- `\f` → Form Feed (page break)  
- `\ooo` → Octal value  
- `\xhh` → Hex value

**Examples:**

```python
txt = "Hello\rWorld!"  # Erases one character (backspace)
print(txt)

txt = "Hello \bWorld!"  # A backspace character
print(txt)

txt = "\110\145\154\154\157"  # Octal value for "Hello"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"  # Hex values for "Hello"
print(txt)

txt = "Line1\fLine2"  # Form feed (page break), moves to the next page (used in printers)
print(txt)
```

---

#### **Unicode characters:**

Unicode characters are denoted by `\u` followed by a four-digit hexadecimal code.

```python
print(r"\u0041")  # A
print(r"\u0042")  # B
print(r"\u0043")  # C
```
# globl stuffs
<!-- 
---
dis : a py built in module is disassembleIn Python, everything is treated as an objectFeature
`dir()` → returns **list of names** (attributes, methods) for:
- Object (if given)
- Current scope (if no argument)  
Useful for **exploring** objects. 🚀
string_methods: str = dir(set)
# Filter out methods starting with "__"
filtered_methods: str = [method for method in string_methods if not method.startswith("__")]
print(filtered_methods)
type() instead of .typeOf()
id(): every thing is storing in a unique location with some address  so to see that address  we use id()
len() instead of .lenght()
pass to pass the logic means we will write logic it later
d -->
## Match cses
<!-- match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (similar to "else")
variable: The value being matched.
pattern1, pattern2: Patterns to match against.
_: A wildcard pattern that matches anything (acts as a default case).
i thin match case isnt if-elif-else chain it is if-if-if-& else 

we can use else in for loop it wil work only when there is no break in for loop if there is a break so it wont run 

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!")  # This will NOT run
 -->

# third parameter Of range()
 <!-- ### The **third parameter** in `range(start, stop, step)` is the **step size**.

- **Step** controls how much to increment or decrement the value at each iteration.
For example, `range(2, 11, 2)` means:
- Start at `2`.
- Go up to (but don't include) `11`.
- **Step by 2** (skip 1, take every 2nd number).

In this case, `range(2, 11, 2)` gives: `2, 4, 6, 8, 10`.

If you change the step:
- `range(1, 10, 3)` → will give `1, 4, 7` (steps of 3).
- `range(10, 1, -1)` → will give `10, 9, 8, 7, 6, 5, 4, 3, 2` (steps of -1, counting down).

So, the third parameter controls how "big" each step is in the sequence.
 -->

 <!-- _ (underscore) This is a throwaway variable, which is a common Python convention for a variable that you don't plan to use
for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    print(f"Hello, World! Iteration { _ }")

break: Exits the loop immediately.
continue: Skips the rest of the code in the current iteration and moves to the next iteration. -->


