
#  3) write a function with 2 arguments , second argument should be "default argument" and display them. Using
#  a) normal function 
#  b) lambda

# def disp(a,b="default argument"):
#     print(a,"   ",b)

# disp(2) #functio call

######Lambda###

disp=lambda a,b="default argument":print("given arguments are" ,a,"and",b)

disp(10)   #function call
disp(5,6)

