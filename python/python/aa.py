a=5
for i in range(1,5):
    num=1
    for j in range(5,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
            num+=1
    print("")
