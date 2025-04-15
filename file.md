Quick diff:

- **`dis`** → Disassembles Python bytecode. Used for debugging/inspection.  
`dis` : a py built in module is disassembleIn Python, everything is treated as an objectFeature
  ```python
  import dis
  dis.dis("a = 1 + 2")
  ```

- **`decode`** → Converts **bytes → string** using a character encoding (like UTF-8).  
  ```python
  b = b'hello'
  print(b.decode('utf-8'))  # 'hello'
  ```

✅ `dis` = inspect code; `decode` = convert bytes to string.
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
## Match cases
```python 
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (similar to "else")
```
 match: A statement that checks the value of a variable against multiple patterns.
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
# _ 
 _ (underscore) This is a throwaway variable, which is a common Python convention for a variable that you don't plan to use
for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    print(f"Hello, World! Iteration { _ }")

# loops
break: Exits the loop immediately.
continue: Skips the rest of the code in the current iteration and moves to the next iteration. 

# Validate email:
import re
email = "test@example.com"
print(bool(re.match(r".+@.+\..+", email)))  # True
# Strong password check:	
import re
password = "Abc123!"
print(bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}$', password)))  
# True if 6+ chars, letters & numbers 
