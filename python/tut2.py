# now we learn about the list in detail in python
# list is  a collection of item 
# In Python, a list is a built-in ordered, mutable, and iterable data structure that can hold a collection of items. These items can be of any data type (integers, strings, other lists, etc.).
# | Operation | Example                    | Description                 |
# | --------- | -------------------------- | --------------------------- |
# | Access    | `my_list[0]`               | Get first item              |
# | Modify    | `my_list[1] = 99`          | Change second item          |
# | Append    | `my_list.append(4)`        | Add to the end              |
# | Insert    | `my_list.insert(2, "new")` | Insert at index             |
# | Remove    | `my_list.remove("hello")`  | Remove by value             |
# | Pop       | `my_list.pop()`            | Remove and return last item |
# | Length    | `len(my_list)`             | Get number of items         |
# | Slice     | `my_list[1:3]`             | Get a sublist               |
# | Sort      | `my_list.sort()`           | Sort the list in place      |
# | Reverse   | `my_list.reverse()`        | Reverse the list in place   /
# | Clear     | `my_list.clear()`          | Remove all items            |  
my_list = [1, 2, 3, "hello", True]
print(my_list)  # Output: [1, 2, 3, 'hello', True]
my_list.append(4)  # Add 4 to the end
print(my_list)  # Output: [1, 2, 3, 'hello', True, 4]
my_list.insert(2, "new")  # Insert "new" at index 2
print(my_list)  # Output: [1, 2, 'new', 3   , 'hello', True, 4]
print(my_list[0])  # Access first item: Output: 1
my_list[1] = 99  # Modify second item
print(my_list)  # Output: [1, 99, 'new', 3, 'hello', True, 4]
my_list.remove("hello")  # Remove item by value
print(my_list)  # Output: [1, 99, 'new', 3, True, 4]
my_list.pop()  # Remove and return last item
print(my_list)  # Output: [1, 99, 'new', 3
my_list.reverse()  # Reverse the list in place
print(my_list)  # Output: [3, 'new', 99, 1
my_list.sort()  # Sort the list in place (only works for comparable items)
print(my_list)  # Output: [1, 3, 'new', 99
my_list.clear()  # Remove all items
print(my_list)  # Output: []
l=[1, 2, 3, 4, 5]
print(max(l))  # Output: 5
print(min(l))  # Output: 1
print(sum(l))  # Output: 15
print(sum(l))
# Output: 15
print(len(l))  # Output: 5
# if change one value is list with ohter data type then it will give errror
#  for htat i have to convert the list to string
