# Python vs TypeScript/JavaScript: A Beginner-Friendly `Data Types` Comparison

![Data Types](./public/datatype.png)

| Python 🐍                    | TypeScript/JavaScript 🟦|
| ---------------------------- | -----------------------------|
## ***STRING***

| `name: str = "Ali"`          | `let name: string = "Ali";`|


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