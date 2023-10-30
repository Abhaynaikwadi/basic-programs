n = int(input("enter the number"))
reverse = 0
while n>10:
    r = n % 10
    reverse = (reverse*10)+ r
    n //= 10
print("rev no is",reverse)
