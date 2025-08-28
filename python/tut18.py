# s="""Hi,
# i am learning python """
# print(s)
# An f-string is just a string prefixed with f or F, and inside {} you can put variables, expressions, or even function calls
# name="Anshul"
# age=20
# print(f"my name is {name} and i am {age} years old.")
# now we learn about the string operations\
# s1="geeksforgeeks"
# s2="geeks"
# print(s2 in s1)
# print(s1 in s2)
# now we learn about the concatenation in string
# s1="geeks"
# s2="forgeeks"
# s3=s1+s2
# print(s3)
# finding postion of a substring
# now we lean about the index
# what is index?
# The index() method is used to find the position (index) of the first occurrence of a value inside a string or a list
# string.index(substring, start, end)
# list.index(element, start, end)

# What it does: rindex searches from the right (end of the string) and returns the index of the last match (still as a 0-based index from the start).

# s1 = "geeksforgeeks"
# s2 = "geeks"

# # Find the first occurrence of a character (must be a string)
# print(s1.index("e"))        # -> 1 (first 'e' at index 1)

# # Find the last occurrence of a substring
# print(s1.rindex(s2))        # -> 8 (last "geeks" starts at index 8)

# # Search within a range [start, end) — end is exclusive
# print(s1.index("geeks", 1, 13))  # -> 8 (finds the "geeks" at 8 within 1..12)

# # Safer alternatives that don't raise on failure:
# print(s1.find("x"))         # -> -1 (not found)
# print(s1.rfind("x"))        # -> -1 (not found)
# now we learn about the more methods in string operations
# s1="anshul"
# print(len(s1))
# s2=s1.upper()
# print(s2)
# s3=s2.lower()
# print(s3)
# print(s1.islower())
# print(s2.isupper())
# now we learn about the comparison in python
# s1="anshul"
# s2="jagota"
# print(s1==s2)
# print(s1!=s2)
# print(s1<s2)
# print(s1>s2)
# print(s2==s1)
# now we learn about the searching in python
# txt=input("enter the string:")
# pat=input("enter the pattern:")
# per=txt.find(pat)
# while per!=-1:
#     print("Pattern found at index:", per)
#     per=txt.find(pat, per+1)
# now we learn about the reversing in python
s="anshul"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# now we learn about the string slicing
s2=s[::-1]
print(s2)
