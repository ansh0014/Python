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
def sum(*elements):
    res=0
    for x in elements:
        res=res+x
    return res

print(sum(10,20))
print(sum(10,20,30))
print(sum(10))
print (sum())
