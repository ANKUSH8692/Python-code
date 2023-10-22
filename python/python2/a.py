import random
def gamewin(comp,a):
    if(comp==a):
        print("game is tie")
    elif(comp=='r'):
        if(a=='p'):
            print("u win")
        else:
            print("u lose")
    elif(comp=='s'):
        if(a=='r'):
            print("u win")
        else:
            print("u lose")
    elif(comp=='p'):
        if(a=='s'):
            print("u win")
        else:
            print("u lose")
print("computer chose 1,2,3 ")
r=random.randint(1,3)
if r==1:
    comp='r'
elif r==2:
    comp='s'
else:
    comp='p'
a=input("enter for rock(r),sc(s),paper(p)")
print(comp)
gamewin(comp,a)
