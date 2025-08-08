# now we learn about the sets in detail
# A set is a built-in unordered, mutable, and iterable data structure in Python that can hold a collection of unique items. Sets are useful for membership testing and eliminating duplicate entries.
# Sets are defined using curly braces or the `set()` constructor
# A set is a built-in unordered, mutable, and unindexed collection that only contains unique elements.
# | Feature      | Description                                |
# | ------------ | ------------------------------------------ |
# | Unordered    | Elements have no guaranteed order          |
# | Mutable      | You can add/remove elements                |
# | Unique items | Duplicate values are automatically removed |
# | Unindexed    | No way to access by index like `set[0]`    |
my_set= {1, 2, 3, "hello", True}
print(my_set)  # Output: {1, 2, 3, 'hello', True}
my_set.add(4)  # Add an element
print(my_set)  # Output: {1, 2, 3, 'hello
set.remove(2)  # Remove an element by value
print(my_set)  # Output: {1, 3, 'hello', True, 4}
# | Feature        | Set `{}` / `set()`        | List `[]`              |
# | -------------- | ------------------------- | ---------------------- |
# | Ordered?       | ❌ No (unordered)          | ✅ Yes                  |
# | Indexed?       | ❌ No indexing             | ✅ Yes                  |
# | Duplicates?    | ❌ No duplicates allowed   | ✅ Duplicates allowed   |
# | Mutable?       | ✅ Yes                     | ✅ Yes                  |
# | Use case       | Fast membership checking  | Ordered collection     |
# | Speed (lookup) | 🔥 Very fast (hash table) | Slower (linear search) |
s={1, 2, 3, 4, 5}
print(s)  # Output: {1, 2, 3, 4, 5}
s3={}
print(type(s3))  # Output: <class 'dict'>, empty dictionary
s4=set()
print(type(s4))  # Output: <class 'set'>, empty set     
print(s3)  # Output: {}
print(s4)  # Output: set()
s5={50,30}
s5.add(20)
s5.add(10)
print(s5)  # Output: {50, 20, 30, 10}
s.update ({6, 7, 8})  # Add multiple elements
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
s.discard(3)  # Remove an element if it exists
print(s)  # Output: {1, 2, 4, 5, 6, 7, 8}
s.pop()  # Remove and return an arbitrary element       
print(s)  # Output: {2, 4, 5, 6, 7, 8}, arbitrary element removed
s.clear()  # Remove all elements
s.clear()  # Output: set(), now it's empty
s7={10,20,30,40,50}
print(len(s7))  # Output: 5, number of unique elements
print(10 in s7)  # Output: True, 10 is in the set
print(100 in s7)  # Output: False, 100 is not in the
# why the sets are faster that the list
# because sets are implemented using hash tables, which allow for O(1) average time complexity for membership testing, while lists require O(n) time complexity for the same operation.
# Sets are unordered collections of unique elements, meaning they do not allow duplicate values. This makes
s8={1, 2, 3, 4, 5}
s9={3, 4, 5, 6, 7}
print(s8.union(s9))  # Output: {1, 2, 3, 4, 5, 6, 7}
print(s8.intersection(s9))  # Output: {3, 4,5}
print(s1-s2)
# Output: {1, 2}, elements in s1 but not in s2
print(s2-s1)  # Output: {6, 7, 8},
print(s8&s9)    # Output: {3, 4, 5}, common elements in both sets
f1={2,4,6,8}
f2={4,8}
print(f1.isdisjoint(f2))  # Output: False, f1 and f2 have common elements
print(f1.issubset(f2))  # Output: False, f1 is not a subset of f2
print(f2.issubset(f1))  # Output: True, f2 is
print(f1>f2) # Output: False, f1 is not a superset of f2
# Output: True, f1 is a superset of f2

