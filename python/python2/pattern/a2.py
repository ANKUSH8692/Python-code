a=int(input("enter"))
for i in range(0,a):
    num=1
    for j in range(a+1,0,-1):
        if i>j:
            print(num,end=" ")
            num=num+1
        else:
            print(" ",end=" ")
            
    print(" ")
