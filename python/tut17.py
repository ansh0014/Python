# now we learn about the strings in python
# ord() -> character-> number
#  takes a single character and return its unicode code point integer
# example
# print(ord('A'))
# print(ord('F'))
# print(ord('c'))
# print(ord(" "))
# chr() -> number -> character
# print(chr(65))
# s="geeks"
# print(s)
# print(s[0])
# print(s[-1])
# print(s[-2])
# s="""Hi,
# This is anshul 
# i am leaning this python course
# but i don't like it 
# because i am obssesd with the c++"""
# print(s)
# s='welcome to this shit thapar'
# s="hi,\nthis is ansul"
# print(s)
# ****************************//**********
# String with an escaped space character "\ " (but space doesn't need escaping, so it's just a normal space)
s1 = "A simple\ example"  
# The "\ " here is not a valid escape sequence, so Python just treats it as a space.

# String ending with a single backslash
# We need to escape the backslash itself by writing "\\"  
# Otherwise, Python would think the last backslash is starting an escape sequence
s2 = "backslash at the end\\"

# String containing the literal characters '\' and 'n'
# This is not a newline — it's actually two characters: backslash + n
s3 = "\\n"

# String containing the literal characters '\' and 't'
# This is not a tab — it's actually two characters: backslash + t
s4 = "\\t"

# Printing the strings
print(s1)  # Output: A simple example
print(s2)  # Output: backslash at the end\
print(s3)  # Output: \n
print(s4)  # Output: \t
