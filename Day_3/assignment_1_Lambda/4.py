# 4) write a function with variable no. of arguments and display them. Using
# 	a) normal function
# 	b) lambda


# def fun(*var):
#     for i in var:
#         print(i)


# fun(1,2,'u',"uma",[1,2,3])


###Lambda###

fun=lambda *args :[print(i) for i in args]
fun(1,2,'u') #function call
