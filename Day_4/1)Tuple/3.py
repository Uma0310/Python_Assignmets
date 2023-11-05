# 3) Write a Python program to find the repeated items of a tuple.
mytuple=(1,2,3,3,4,5,5,5)
print("Repeated items are")
for i in mytuple:
    if mytuple.count(i) > 1:
         print(i)
