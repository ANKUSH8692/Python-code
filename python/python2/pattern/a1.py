a=int(input("enter no."))
for i in range(0,a):
    for j in range(0,i+1):
        if(i>j):
            print("*",end="")
        else:
            print(" ")
    print()
