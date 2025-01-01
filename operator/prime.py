def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("no is composite")
            break
    else:
        print("no is prime")
prime(8)