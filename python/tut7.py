# Now we learn arithmetic operators in Python

x = 9
y = 10
z=2

print(x + y)    # Addition: Adds x and y → 9 + 10 = 19
print(x - y)    # Subtraction: Subtracts y from x → 9 - 10 = -1
print(x * y)    # Multiplication: Multiplies x and y → 9 * 10 = 90
print(x / y)    # Division: Divides x by y → 9 / 10 = 0.9 (float division)
print(x // y)   # Floor Division: Divides and returns the integer part → 9 // 10 = 0  interger arthimatic
print(x % y)    # Modulus: Returns the remainder of x divided by y → 9 % 10 = 9
print(x ** y)   # Exponentiation: Raises x to the power of y → 9^10 = 3486784401
print(x-y+(z))
# all the operator show left to right 
# only power operator move the right to left
# now we learn about the logical operator

a = 10
b = 20
c = 30

# Boolean Expression: (a < b) is True, (b < c) is True
# Logical AND → True and True = True
# Short-circuiting: Evaluates second only if first is True
print(a < b and b < c)    # Output: True

# Boolean Expression: (a < b) is True, (b > c) is False
# Logical OR → True or False = True
# Short-circuiting: Does NOT evaluate second because first is already True
print(a < b or b > c)     # Output: True

# Boolean Expression: (a > b) is False
# Logical NOT → not False = True
print(not a > b)          # Output: True

s1=" "
s2=s1 or "Default"
print(s2)
# or in Python returns the first truthy value, or the last value if all are falsy.
# Now we learn identity comparison operators

k = 20
l = k

# 'is' checks if both variables point to the same object in memory
print(k is l)         # True → k and l refer to the same object

# 'is not' checks if both variables do NOT point to the same object
print(k is not l)     # False → because k and l point to the same object

x1 = 10
x2 = 10

# Small integers are cached in Python (-5 to 256), so x1 and x2 refer to same memory
print(x1 is x2)       # True → both point to the same memory location

y1 = "anshul"
y2 = "anshul"

# Python caches short strings (string interning), so both refer to the same object
print(y1 is y2)       # True → both point to the same interned string
 
l1 = [10, 20, 30]
l2 = [10, 20, 30]

print(l1 == l2)  # True → values are the same
print(l1 is l2)  # False → different memory locations

t1 = (10, 20, 30)
t2 = (10, 20, 30)

print(t1 == t2)  # True → same values
print(t1 is t2)  # True (sometimes) → Python **may reuse** immutable objects like tuples

a = 10
b = 10

print(a == b)  # True
print(a is b)  # True → Python caches small integers (-5 to 256)

s1 = "hello"
s2 = "hello"

print(s1 == s2)  # True
print(s1 is s2)  # True → Python reuses short, literal strings

x = None
y = None

print(x == y)  # True
print(x is y)  # True → `None` is a singleton object in Python

s3 = ''.join(['he', 'llo'])  # dynamically created
print(s1 is s3)  # False → different object
