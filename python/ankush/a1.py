def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ",fact)
    
a=int(input("enter the number "))
fac(a)
