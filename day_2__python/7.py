#7) define a function which accepts a string , toggle and return it.
#	[ hint :  use "swapcase()" function of string ]

#function
def toggle_case_change(str):
    toggled_str = str.swapcase()   #used swapcase() function to toggle string
    return toggled_str

#
string_input=input("enter a name")
toggled_result=toggle_case_change(string_input)
print("toggled reuslt is",toggled_result)


