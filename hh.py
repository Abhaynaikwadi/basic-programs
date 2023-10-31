def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nterm = 10

if nterm<=0:
    print("enter positive number")
else:
    print("fibonacci sequnce:")
    for i in range(nterm):
        print(fibo(i))
