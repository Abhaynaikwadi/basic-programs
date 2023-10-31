str = input("enter the string")
l = list(str)
freq = [l.count(ele) for ele in l]
print(freq)
