l=[1,2,3,4,5,6,7,8,9,10]
l2=[]
n=int(input("enter the number"))
l2=l[n-1::-1]
print(l2[::]+l[n::])
