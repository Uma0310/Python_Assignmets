# 1) Write a Python program to count the elements in a list until an element is a tuple.

# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3

my_list = [1, 2, 3, 'a', (4, 5), 6, 7, 8]

count = 0

for i in my_list:
    if type(i) == tuple:
        break            #brk when i is tuple .
    count += 1

print("Number of elements until a tuple is found:", count)

# In this code, we use the type(item) == tuple condition to check if the type of the current item is a tuple, 
# and if it is, we break out of the loop. Otherwise, we increment the count variable to keep track of the 
# number of elements counted until a tuple is encountered.








# 2) create a tuple to store 5 numbers and then sort it in ascending and descending order.


# mytuple=tuple(i for i in range(0,6))
# print(sorted(mytuple))
# print(sorted(mytuple, reverse=True))

# 3) Write a Python program to find the repeated items of a tuple.
# mytuple=(2,'uma','uma',5,5,5,8)

# # repeated_items = [item for item, count in Counter(my_tuple).items() if count > 1] #1 line for below 3 lines
# repeated_items = []
# for i in mytuple:
#     if mytuple.count(i) > 1 and i not in repeated_items:
#         repeated_items.append(i)

# if repeated_items:
#     print("repeated_items:", repeated_items)
# else:
#     print("No repeated items not found ")


