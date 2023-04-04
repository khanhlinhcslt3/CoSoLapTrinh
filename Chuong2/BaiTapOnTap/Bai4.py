import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=(a+b+c)/2
X=s*(s-a)*(s-b)*(s-c)
S = math.sqrt(X)
print("Dien tich=", S)