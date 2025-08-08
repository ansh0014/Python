# now we learn about the loop in python
# write a porgram to print table of a no:
# n=int(input("Enter a no."))
# while(condition):
#     statment
# the is sytax of while loop
# i=0
# while i<5:
#     print("anshul")
#     i+=2
# while True:
#     print(",")   # this is infinite loop

# now we learn about range of no:
# range() is a built-in Python function used to generate a sequence of numbers.
# Syntax: range(start, stop, step)
# If start is not specified, it defaults to 0.
# 'stop' is exclusive — the range goes up to, but does not include, this value.
# 'step' is optional and defaults to 1 (can also be negative).

r = range(5)  # This creates a range object: starts at 0, ends before 5 → [0, 1, 2, 3, 4]

print(r)
# Output: range(0, 5)
# This prints a special range object — it doesn't display the values directly,
# but shows the range definition. It's a memory-efficient object, not a list.

l = list(r)  # Convert the range object to a list to view all its elements

print(l)
# Output: [0, 1, 2, 3, 4]
# Now you can see the actual numbers in the range.
# range(start, stop, step) generates a sequence of numbers
# - start: where the sequence begins (inclusive)
# - stop: where it ends (exclusive)
# - step: the difference between each number (default is 1)

r = range(5)  # This is equivalent to range(0, 5)
print(type(r))  
# Output: <class 'range'>
# Even though it looks like a list, `range` creates a range object — an iterable, not a list.

# Example 1: start=10, stop=20, default step=1
r = range(10, 20)
l = list(r)
print(l)
# Output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# Starts at 10 and ends before 20. Step is 1 by default.

# Example 2: negative to positive
r = range(-2, 2)
l = list(r)
print(l)
# Output: [-2, -1, 0, 1]
# Starts at -2, ends before 2 → goes up to 1

# Example 3: step of 2
r = range(10, 20, 2)
l = list(r)
print(l)
# Output: [10, 12, 14, 16, 18]
# Starts at 10, ends before 20, stepping by 2

# Example 4: descending range using negative step
r = range(20, 10, -3)
l = list(r)
print(l)
# Output: [20, 17, 14, 11]
# Starts at 20, goes down by 3 each time, and stops before going below 10
