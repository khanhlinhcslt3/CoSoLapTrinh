import math
print("Nhap vao hai canh ke goc vuong:")
a=int(input())
b=int(input())
X= a*a+b*b
c = round(math.sqrt(X),2)
print("Canh ke thu nhat:", a,end='')
print(", canh ke thu hai:", b,end='')
print(", co canh huyen:", c)