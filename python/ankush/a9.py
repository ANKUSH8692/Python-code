def pal(s,s2):
    l=len(s)
    l2=len(s2)
    for i in range(0,l):
        for j in range(0,i):
            if(s[i][j]==s2[i][j]):
                s3=1
            else:
                break

    if(s):
        print("pal")
a=input("enter the string")
b=(a[::-1])
pal(b,a)
