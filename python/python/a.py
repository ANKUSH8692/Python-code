a=int(input("enter the number"))
s=0
while(a>=0):
    r=a%10
    s=s+r
    a=a//10
if(s%2==0):
    print("sum is even number")
else:
    print("sum is odd")
    

