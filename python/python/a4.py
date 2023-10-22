a=int(input("enter the number"))
s=0
s1=0
while(a>0):
    r=a%10
    s=s+r*r
    a=a//10
    while(s>0):
        r1=s%10
        s1=s1+r1*r1
        s=s//10
        
if (s1==1):
    print("Happy number")
else:
    print("not a happy no.")
   
