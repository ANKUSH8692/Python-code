def even(a):
    c=0
    for i in range(2,a+1):
        if(a%i==0):
            c=c+1
    if(a>=1):
        print("True")
    else:
        print("False")
        
l=int(input("enter the number"))        
even(l)
