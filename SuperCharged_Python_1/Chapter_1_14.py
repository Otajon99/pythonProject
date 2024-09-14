def pr_fibo(n):   #Fibonacci sequence
    a, b=1, 0
    while a<n:
        print(a, sep=" ")
        a, b=a+b, a     # a=a+b    b=a     b is equal to oldest value of a


pr_fibo(100)