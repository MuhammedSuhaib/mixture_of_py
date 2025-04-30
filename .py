# import builtins, keyword

# # 1 ) Hard keywords  – absolutely forbidden
# hard = set(keyword.kwlist)

# # 2 ) Soft keywords – legal but confusing
# soft = set(keyword.softkwlist)

# # 3 ) Built‑ins (functions, types, exceptions) – legal but risky
# built_in = set(dir(builtins))

# discouraged = soft | built_in   
# for name in discouraged:
#     print(name)
# import keyword
# print(keyword.kwlist)
# import builtins
# print(dir(builtins))  # Display built-in functions, types, and exceptions

# # Print each built-in item
# for item in dir(builtins):
#     print(item)
# bugs = "👾👾👽"
# code = f"want, {bugs}"
# print( code) #want, 👾👾👽

# txt = "I want {} and then {}".format("coffee", "tea")
# print(txt)
# lambda arg1, arg2: arg1 + arg2
# # Example of passing arguments to lambda function
# add_numbers = lambda arg1, arg2: arg1 + arg2
# result = add_numbers('1', '2')
# print(result)
# Create a generator expression that multiplies each number by 2
# gen = (x * 2 for x in range(3))
# for x in range(3):
#     print(x )

#     print('>>>',x * 2)

# # Print the type of 'gen', it will show it's a generator
# print(type(gen))

# # Iterate over the generator
# for value in gen:
#     # Print each value generated
#     print(value)