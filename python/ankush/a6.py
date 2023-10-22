a=input("enter the string")
l=len(a)
l1=[]
for i in range(0,l):
    if(a[i]==" "):
        break
    else:
        l1.append(a[i])
if "a" in l1:
    print("a",end="")
if "e" in l1:
    print("e",end="")
if "i" in l1:
    print("i",end="")
if "o" in l1:
    print("o",end="")
if "u" in l1:
    print("u",end="")
print(l1)
