Use the slice Operator
You can also make a copy of a list by using the : (slice) operator.

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

adding gloable  keyword before var name inside a function making that local var global & it will be accesibly outside also
`return` exits the function and gives back a value to the caller. It can be stored in variables for future use.


	

Feature	Python (lambda)	JavaScript/TypeScript (=>)
Syntax	lambda args: expression	(args) => expression
Multi-line?	❌ (One-liner only)	✅ (Supports blocks {})
Scope	No return, only expressions	Supports {} with return

		million dora trick
 
def add(*nums):
    return sum(nums)

print(add(1, 2, 3))  # 6

		 Validate email:


import re
email = "test@example.com"
print(bool(re.match(r".+@.+\..+", email)))  # True

		Strong password check:	
import re
password = "Abc123!"
print(bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}$', password)))  
# True if 6+ chars, letters & numbers


In Python, "guards" usually mean:


bcz 2nd parma never reach that value so in order to reach that instead of write a number ahead we can do it like 1+10 now it can reach reach 10 even it is a variable

the the pram will add that number in each itration like 
num, = 10

 for i in range (1, 1+num,3):
 print( i )#1,4,710


\r = carage treturn it remove prevous words == doublesecet & move on





Ordered: Lists are ordered, meaning that the items in the list have a specific order and can be accessed by their index.
Mutable: Lists are mutable, meaning that they can be modified after they are created.
Indexed: Lists are indexed, meaning that each item in the list has a specific index that can be used to access it.
Dynamic size: Lists can grow or shrink dynamically as elements are added or removed.
Heterogeneous: Lists can contain elements of different data types, such as integers, strings, floats, and other lists.
Supports duplicate values: Lists can contain duplicate values.

fruits: list = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple, accessing element in reverse order


append vs extend 
apnd 4 single value | x6tnd  4 multiple elemnts

Feature | pop() | remove()
Based on | Index | Value
Return value | Yes (removed item) | No (returns None)
Error if... | Index out of range | Value not found
Default use | Removes the given index item if not given so last item | Removes first matching value


pop give error if not found but ve can handle it grace fully on the 2nd index where we ca n define what to say if not found either -1 or any other msg like "No such item found"
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
warnig:

You can't do it with a single remove().
remove() deletes only first match.

To remove all, you must loop or use list comprehension.



Here’s both ways ⚡:

**Loop way**  
```python
lst = [1, 2, 1, 3]
while 1 in lst:
    lst.remove(1)
```

**List comprehension way**  
```python
lst = [x for x in lst if x != 1]
```
also we can do this with filter

lst = list(filter(lambda x: x != 1, lst))

			Sort


	Ascending Order
numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
	Descending Order
numbers.sort(reverse=True) or numbers.reverse()
	String Length (shortest one first)
words.sort(key=len)
	String Length (longest one first)
words.sort(key=lambda word: word[-1])



			Using list comprehension
List comprehension is a powerful feature in Python that allows you to create new lists in a concise way. It's a compact way to create lists from existing lists or other iterables by applying a transformation or filter to each element.
Syntax
new_list = [expression for element in iterable if condition] (if condition is opnitional)

Python  to store collections of data using
1>> Tuple
2>> Set
3>> List
4>> Dictionary
# Tuple 
**Hashable**: Tuples can be used as keys in dictionaries because they are immutable.
👑 **allow duplicate** Tuples allow duplicate values:


Even though tuples are immutable, Python may create new instances in memory when you define identical tuples in separate assignments. This is why id(tuple_1) and id(tuple_2) may differ.
id(tuple_1) =  139975700916672
id(tuple_2) =  139975700971648
tuple_1 == tuple_2 =  True

## working methods on tuples

we can`t modify tuple but create a new tuple from that with the 
modification 
like i did 
```py
# Tuple slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1
treter = tuple2[1:] #tuple2[1:] = (20, 30)
print("🎈",treter , type(treter)) # 🎈 (20, 30) <class 'tuple'>
 ```
 also 
**tuple + tuple = tuple**
```py
using dir() without "__"
it only give 2 mtds 
1: 'count'
2: 'index'
```
```py
tuple3: tuple = tuple1 + tuple2 
print("tuple1 + tuple2 =", tuple3)#tuple1 + tuple2 = ('apple', 'banana', 'cherry', 10, 20, 30)
 ```
**tuple nesting is different form tuple concatenation**
```py
# Nested tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple) #(('apple', 'banana', 'cherry'), (10, 20, 30))
means 2 tuples (),() inside a tuple () ==> ((),())
 ```
 # Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)


# Unpacking tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)
# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

## forbidden methods on tuples
tuple1.sort()
tuple1.reverse()
tuple1.append("mango")
tuple1.extend(["grape", "kiwi"])
tuple1.remove("banana")
deleted = tuple1.pop(1)

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple. -------------
                    |
```py               v 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")#tuple
print(type(thistuple))#str
```
It is also possible to use the tuple() constructor to make a tuple.

```py
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

# Dict

Un-indexed: Items are accessed using keys, not indices.
Without duplicates: Keys must be unique, but values can be duplicated.
**way to access** car["model"] no dots here
but There is also a method called get() that will give you the same result

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
**way to add new key/vl pari or to modify existing key** # Add person["email"] = "alice@example.com"

It is also possible to use the dict() constructor to make a dictionary.

```py
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
The items() method will return each item in a dictionary, as tuples in a list.
```py
x = thisdict.items()# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```
**fromKeys()**
Syntax
dict.fromkeys(keys, value)
Parameter Values
Parameter	Description
keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None
```py
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)#{'key1': 0, 'key2': 0, 'key3': 0}
```

## Python dict comprehension syntax
```py
{key: value for item in iterable}
```
```py
celsius_temps = [0, 10, 20, 30, 40]
fr = {str(r) + "c": str((r * 9/5) + 32) + "f" for r in celsius_temps}
```

# set
A set is:

unordered
unindexed
mutable
but unique 🌟
Note: to create an empty set you have to use set(), not {}
can create using set constructor set() like: my_set2: set = set([123, 452, 5, 6])
✔ A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. 

❌If you try to put a list or a dictionary in the set collection, Python raises a TypeError.<!-- TypeError: unhashable type: 'list -->
"Python sets are unordered collections,the way elements are stored in memory depends on hashing, which can lead to unpredictable ordering. but from hash point of view they r orderd"
since set os unorder so we cant  call them, from their indexs 
also set object does not support item assignment my_set[0] = 10

```py
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'} 
# Remove an item
my_set.remove(3)# Output: {1, 2, 4, 5 , 'A','a'}
my_set.remove('A') # Output: {1, 2, 4, 5,'a'}
my_set.add(6)# Output: {1, 2, 4, 5, 6}
#discard() only removes a single element otherwise accepted 1 arg but got 3
```
to take union() of two sets: we use union() method or 
The | operator is a binary operator that can be used to combine two sets into a single set. It has the same effect as the union() method, but is often more concise and readable.
```py
my_set: set   = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}
my_set3: set  = my_set.union(my_set_2)
my_set3: set  = my_set | my_set_2 #same output
```
remove() vs discard() vs difference_update() methods:

remove() method:

The remove() method removes the specified item from the set.
If the item is not found in the set, it raises a KeyError.
This method is suitable when you are sure that the item exists in the set.
discard() method:

The discard() method also removes the specified item from the set.
However, if the item is not found in the set, it does not raise any error. It simply does nothing.
This method is suitable when you are not sure if the item exists in the set.

difference_update() to remove multiple items at once 
```py
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("Before: my_set = ", my_set)
my_set.difference_update({1, 5, 3, 'A'})
print("After:  my_set = ", my_set)

```
**The Hashing**
Hashing is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only immutable objects are hashable.

Immutable data types in Python come with a built-in method for computing their hash value, which is called hash.

A hash table is a data structure that can map keys to values and that implements a hash function to compute the index to an array of buckets or slots
```py
a: str = "Hello! World"
b: str = "Hello! World"

print("id(a) = ", id(a))#id(a) =  132467750244336
print("id(b) = ", id(b))#id(b) =  132466877525360
print("hash(a) = ", hash(a))#hash(a) =  9090330697819382555
print("hash(b) = ", hash(b))#hash(b) =  9090330697819382555
print("hash(a)      = ",hash(a))#hash(a)      =  9090330697819382555
print("a.__hash__() = ", a.__hash__()) # __dunder__() output is same here
```
Even if a set only allows immutable items, the set itself is mutable.
In Python, a dictionary key must be an immutable object, meaning its value cannot be changed after it's created. This is because dictionaries use a hash table to store key-value pairs, and mutable objects cannot be hashed.
& wecant store set in dict`s keys

adding/removing elements may trigger rehashing, leading to reallocation of storage

Sets are unordered, but as of Python 3.7+, they maintain insertion order while internally relying on hashing."
