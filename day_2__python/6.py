#6) define a function which accepts a character and return toggle of it. 
#toggle means covert upper to lower and lower to upper case


#fuction
def toggle_case_check(char):
    if char.isupper():
        return char.lower()
    elif char.islower():
        return char.upper()

    
cc= (input("Enter a character "))
c=ord(cc)
if (c>=97 and c<= 122) or (c>=65 and c<=90):
    toggled_char=toggle_case_check(chr(c))
    print("Toggled character is:",toggled_char)
else:
    print("Wrong input")




    

