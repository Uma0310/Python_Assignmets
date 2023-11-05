#1) Write a Python program to count the elements in a list until an element is a tuple.

list=[1,'a',3,4,(5,6,7),"uma"]

counter=0
for i in list:
    if (type(i)==tuple):
        break
    counter+=1
    
print(counter)

    
