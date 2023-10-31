name = input("enter the string")
str = ""
for i in name:
    str = i+str
print("reverse string is:",str)
if str == name:
    print("palindrome")
else:
    print("not palindrome")
    
    
