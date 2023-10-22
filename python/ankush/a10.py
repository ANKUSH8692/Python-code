def lc(c,d):
    for i in range(1,c):
        if(c%i==0):
            for c in range(1,d):
                if(d%c==0):
                    print(d)
                    break
a=int(input("enter"))
b=int(input("enter"))
lc(a,b)
''' def cal(a,b):
if(a>b):
grater =x
else:
greater=y
while(true)
if((greater%x==0)and (graeter%y==0)):
break:
greater+=lreturn lcm
