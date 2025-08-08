# a = int(input("Enter a number: "))

# if a == 1:
#     for i in range(1, 11):
#         res = a * i
#         print(res, end=" ")

# elif a == 2:
#     for i in range(1, 11):
#         res = a * i
#         print(res, end=" ")

# elif a == 3:
#     for i in range(1, 11):
#         res = a * i
#         print(res, end=" ")

# else:
#     print("Aukat ke bahar hai yeh question, Anshul ne itna hi develop kiya hai mujhe.")
# range(start, stop, step)
# start → (optional) starting value (default is 0)

# stop → (required) end value (exclusive)

# step → (optional) increment/decrement (default is +1)

# real world example of nested loop
ll=[[10,20,30],[40,50,60],[80,70]]
for l in ll:
    for x in l:
        print(x, end=" ")
    print()    