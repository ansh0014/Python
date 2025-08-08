# now we learn membership test operateors
# string:check for substring
# Disctionary: check for key
# list , set, Tuple etx : check for memembership
ch = 'b'
print(ch)         # b
print(len(ch))    # 1 → length is 1, so it behaves like a character
s="anshul"
print("a" in s)
print("k" in s )
print("h" in s )
d={10:"abc", 20:"efg"}
print(10 in d)
print(15 in d)
print("abc" in d)
l=[10,30,50]
print(10 in l)
print(60 in l)
print(60 not in l)
