# # 1) Create a multi-level inheritance , override default constructors in the child classes ,
# # instantiate the child class and show how will u
# #  invoke parent class constructor from child class ?

# class Base:
#     def __init__(self):
#         print("in Base class constructor")

# class sub(Base):
#     def __init__(self):
#         super().__init__()
#         print("in sub class constructor")

# s1=sub()


# 2) create a class "Vehicle", define a method "public void start()" in it. From this class derive a class FourWheeler. 
# How will u override "start()" method of parent class ?
# class Vehicle:
#     def start(self):
#         print("Class Vehicle")

# class FourWheeler(Vehicle):
    
#     def start(self, num1):
#         print("fourWheeler start method",num1)


# f1=FourWheeler()
# f1.start(100)



# 3) Go for Hierarchical inheritance, create instances of child class and observe constructor invocation.
# class Base:
#     def __init__(self,num):
#         print("in Base class constructor")
    
# class Sub1(Base):
#     def __init__(self):
#         super().__init__(self)
#         print("in sub1 class constructor")

# class Sub2(Base):
#     def __init__(self):
#         super().__init__(self)
#         print("in sub2 class constructor")
    
# s1=Sub1()
# print(id(s1))
# s2=Sub2()
# print(id(s2))

# 4) Create a class "Top1" with "disp1()" method.
# From this class Derive "Bottom1", "Bottom2" and "Bottom3" classes ,override the "disp1()".
# create a function "perform" which can take argument as object of any child class.
# Now show how will u achieve dynamic polymorphism.

class Top1:
    def disp1():
        print("in Top1")

class Bottom1(Top1):
    def disp1():
        print("in bottom1")

class Bottom1(Top1):
    def disp1():
         print("in bottom2")



# 5) create Base class and Sub class with parameterized constructors. 
# Show how will you invoke Base class parameterized constructor from Sub class.



