from math import *

x = int(input())


M1 = ceil(pow(x,(5/3))+tan(radians(x)))
M2 = floor(pow(pi,(2+atan(pow(sin(radians(x)),2)))))
print(gcd(M1,M2))