a=int(input("enter the"))
a1=a
s=0
while(a>0):
    fact=1
    c=0
    c=a%10
    while(c>0):
        fact=fact*c
        c=c-1
    s=s+fact
    a=a//10
print(s)
