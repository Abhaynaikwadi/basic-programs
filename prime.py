def prime(num):
    if num > 1:
        for n in range(2,num):
            if num % n == 0:
                print(num,"not prime")
                break
                
        else:
            print(num,"prime no")
            break
    else:
        print(num,"not prime")
prime(5)
