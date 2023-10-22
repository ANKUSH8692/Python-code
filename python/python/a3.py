import re
txt="the rain in spain"
y=re.split("\s",txt,2)
z=y[0]+" "+y[1]
y.remove("the")
y.remove("rain")
y.insert(0,z)
print(y)
