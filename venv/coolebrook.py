import math
e=0.0015
d=100
Re=100000
f1=0.02
f2=(2*math.log10(e/d/3.71+2.51/Re/math.sqrt(f1)))**(-2)
while (math.fabs(f2-f1)>0.000000000001):
    f1=(2*math.log10(e/d/3.71+2.51/Re/math.sqrt(f2)))**(-2)
    break    
print(f1)