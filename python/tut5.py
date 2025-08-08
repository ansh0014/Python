# now we learn about the dictionary in python
# A dictionary (or dict) in Python is an unordered, mutable, and indexed collection that stores key-value pairs
my_dict={
    "name": "Anshul",
    "age": 25,
    "is_valid": True,
    "marks": 90,
    "pi": 3.14,
    "city_name": "Noida"
}
print(my_dict)  # Output: {'name': 'Anshul', 'age': 25, 'is_valid': True, 'marks': 90, 'pi': 3.14, 'city_name': 'Noida'}
print(my_dict["name"])  # Accessing value by key: Output: Anshul
print(my_dict["age"])  # Output: 25 
# now we learn about the type conversion in python
# their is type converseion in implicit type conversion
a=10
b=1.5
c=a+b   # this is implicit type conversion 
print(c)
# now we learn about the explicit type conversion
s="10"
i=10+int(s)
print(i)
k="anshul"
print(list(k))
print(tuple(k))
print(set(k))  # Output: {'a', 'h', 'l', 'n
