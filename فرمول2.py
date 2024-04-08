
import math
x = int(input())
y = math.floor(math.pow(math.e, math.asin(math.pow(math.cos(math.radians(x)), 2))))
print(math.gcd(x, y))