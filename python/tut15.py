# # now we learn about the function
# def f( a, b):
#     return a+b

# a=9
# b=8
# res=f(a, b)
# print("ans:", res)
# def printDate(d, m, y):
#     print(d, m, y, sep="-")
# print("India became independent")
# printDate("15","08","1947")
# Application
# Avoid code Redundancy and Ease Maintenance
# Make code modular
# takeInput()
# processData()
# ProduceOutput()
# Abstraction
# avoid variable name collision
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

# n = int(input("Enter a number: "))
# res = fact(n)
# print("Factorial:", res)
# f is used for the formatting the string 
# def sum(*elements):
#     res=0
#     for x in elements:
#         res=res+x
#     return res

# print(sum(10,20))
# print(sum(10,20,30))
# print(sum(10))
# print (sum())
# now we learn about the length Arugments
# def printElements(*elements):
#     print(elements)
# printElements(101,"abc",100)
# printElements(102,"gbc",200)
# Variable- length arguments mean you can pass any number of arguments to a fucntion-not fixed in advanced
# more examples
# def show_number(*nums):
#     print(nums)
# show_numbers(1,2,3)   #(1,2,3)
# show_numbers(10,20)  # (10,20)
# show_numbers(5)
# ** Kwargs variable length keyword arugments
"""
📌 Variable-Length Keyword Arguments (**kwargs) and .items()

1. **kwargs in a function definition allows it to accept any number
   of keyword arguments. All keyword arguments are packed into a
   dictionary where:
      - Keys   → argument names
      - Values → argument values

   Example:
       def func(**data):
           print(data)

       func(name="Anshul", age=21)
       # data = {'name': 'Anshul', 'age': 21}

2. The .items() method:
   - Belongs to the built-in dict (dictionary) class in Python.
   - Returns all dictionary key-value pairs as tuples in a special
     view object called dict_items.

   Example:
       data = {'name': 'Anshul', 'age': 21}
       print(data.items())
       # dict_items([('name', 'Anshul'), ('age', 21)])

3. Why use for key, value in data.items():
   - Iterates over each (key, value) tuple from the dictionary.
   - Unpacks each tuple into variables 'key' and 'value' inside the loop.

4. The dot (.) operator in Python:
   - Works like in C++/Java: used to access attributes or methods of an object.
   - Here, 'data' is a dictionary object, and 'items' is one of its methods.
   - Writing data.items() means: call the 'items()' method of the dictionary object 'data'.
"""

# collect extra keyword 
# collect extra keyword arguments using **details
def student_profile(**details):
    print("Student Profile")

    # details is a dictionary containing all keyword arguments
    # .items() is a built-in dictionary method that returns
    # all key-value pairs as tuples in a special 'dict_items' view object.
    # Example: if details = {"name": "Anshul", "age": 21}
    # then details.items() = dict_items([('name', 'Anshul'), ('age', 21)])
    # The for loop unpacks each (key, value) tuple into variables
    # 'key' and 'value' so they can be used directly in the loop.
    for key, value in details.items():
        print(f"{key.capitalize()}:{value}")

# passing different keyword arguments
student_profile(name="Asnhul", age=21, course="B.Tech", city="Delhi")
print()
student_profile(name="Priya", course="MCA", gpa=9.1)

# **details  → dictionary  → .items()  → (key, value) in loop
