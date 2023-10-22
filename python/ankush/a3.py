def ma(a,b):
    if(a>b):
        return a
    else:
        return b
def max3(a,b,c):
    return max(a,max(a,b))
print(max(1,2,3))
a=int(input("enter the number 1st"))
b=int(input("enter the number 2st"))
c=int(input("enter the number 3st"))
ma(a,b,c)
