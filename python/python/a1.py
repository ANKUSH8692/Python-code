
a=int(input("enetre the number"))
for i in range(0,a):
    n=1
    for j in range(a,0,-1):
       if(j>i):
           print("",end=' ')
       else:
           print(n,end=' ')
           n+=1
    print(" ")
 # pattern   
a1=int(input("enetre the number"))
for i1 in range(0,a1):
    n1=1
    for j1 in range(a1,0,-1):
       if(j1>i1):
           print(" ",end=' ')
       else:
           print(n1,end=' ')
           n1+=1
    print(" ")

# paat
a2=int(input("enter the pattern"))
for i2 in range(1,a2+1):
    for j2 in range(1,i2+1):
        print(j2,end=" ")
        
    print(" ")










     
