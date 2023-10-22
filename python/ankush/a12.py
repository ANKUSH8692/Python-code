def la(s):
    for i in range(s):
        a=s[i]
        b=s[i]+1
        if(b>a):
            a=b
    print("l",a)
l=[5,4,8,9,10,5,6,-1,-5]
la(l)
