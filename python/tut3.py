# now we learn about the tuple in detail in python
# A tuple is a built-in ordered, immutable, and iterable data structure in Python that can hold a collection of items. Tuples are similar to lists but cannot be modified after creation.
t=(1, 2, 3, "hello")
print(t)  # Output: (1, 2, 3, 'hello')
# Tuples are defined using parentheses
# Accessing items
print(t[0])  # Output: 1
# Modifying a tuple is not allowed, so the following line would raise an error
# t[1] = 99  # This will raise a TypeError
t=()
print(t)  # Output: ()
print(type(t))
t=(10)
print((type(t)))  # Output: <class 'int'>, not
# a tuple, just an integer
t=(10,)  # Adding a comma makes it a tuple
print(type(t))  # Output: <class 'tuple'>, now it's a tuple
# Tuples can contain mixed data types
t=(1, "hello", 3.14, True)
print(t)  # Output: (1, 'hello', 3.14, True
# Tuples can be nested
nested_tuple = (1, (2, 3), "hello")
print(nested_tuple)  # Output: (1, (2, 3), 'hello')
t=10,20,30,40,10
print(t)  # Output: (10, 20, 30, 40, 10)
print(t[2])
print(t[-1]) # Output: 10, accessing the last item
print(t[1:4])  # Output: (20, 30, 40), slicing the tuple
# sequence[start:stop] this is the syntax for slicing
