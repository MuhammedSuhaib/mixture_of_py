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
