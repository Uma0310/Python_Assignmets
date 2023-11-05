# # """ 1) write a function to accept a number and return its square using
# # 	a) normal function
# # 	b) lambda """

# # #
# def sqr(a):
#     return a*a

# #
# num=int(input("enter a number"))
# b=sqr(num)
# print(f"squre of {num} is",b)

# #LAMBDA
# #
sqr= lambda x: x**2
#
num=int(input("Enter a number"))
b=sqr(num)
print(f"square of number{num} is",b)


#orrrr sytax for lambda
sqr= (lambda x: x**2) (num)

