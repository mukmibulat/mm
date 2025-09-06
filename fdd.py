from math import*
a=float(input())
z1=1-0.25*(sin(2*a)*sin(2*a))+cos(2*a)
z2=cos(a)**2+cos(a)**4
zz1=round(z1,3)
zz2=round(z2,3)
print(zz1,zz2)