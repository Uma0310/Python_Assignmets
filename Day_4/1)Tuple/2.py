#2) create a tuple to store 5 numbers and then sort it in ascending and descending order.
mytuple=(8,6,10,45,5)
print(mytuple)

a=tuple(sorted(mytuple))
b=tuple(sorted(mytuple,reverse=True))
print(a,b)


