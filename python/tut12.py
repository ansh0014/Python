# # Now we learn about the loop

# # 🔁 For loop in Python:
# # Syntax:
# # for x in sequence:
# #     statement 1
# #     statement 2
# #     ...

# # "sequence" can be a list, string, tuple, set, range, etc.

# # Example 1: Looping through a list
# l = [10, 20, 30, 40]
# for x in l:
#     print(x)
# # Output:
# # 10
# # 20
# # 30
# # 40
# # 👉 Here, 'x' takes each element from the list one by one

# # Example 2: Looping through a string
# s = "gfg"
# for x in s:
#     print(x)
# # Output:
# # g
# # f
# # g
# # 👉 Strings are iterable; each character is processed one by one

# # Example 3: Looping using range()
# for x in range(5):
#     print(x)
# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4
# # 👉 range(5) generates numbers from 0 to 4

# # Example 4: Conditional inside for loop
# for x in range(20):
#     if x % 6 == 0:
#         print(x)
# # Output:
# # 0
# # 6
# # 12
# # 18
# # 👉 This prints numbers divisible by 6 in the range 0–19

# # Example 5: Looping using index (via range + len())
# l = [10, 20, 30, 40]
# for i in range(len(l)):  # len(l) is 4, so range(4) = [0, 1, 2, 3]
#     print(l[i])
# # Output:
# # 10
# # 20
# # 30
# # 40
# # 👉 'i' is the index (0 to 3), and l[i] accesses the element at that index

# Q. n=3 give me table
n=int(input("Enter a no:"))
# i=1
# m=int(input("Enter a no:"))
# while i<=m:
#     print(i*n)
#     i+=1
# while i<=10;
# print(i*n)
# i+=1
# for i in range(1,11):   # range (1,x) 1,2,to x-1
#     print(i*n)

# now we learn about the break statment in python
# find the smallest divisor of a number such that the divisor is greater than 1

for i in range(2, n+1):
    if n%x==0
    print(x)
    break