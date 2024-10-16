o=int(input())
x=o+1
y=1
while x!=5:
    x=x-1    
    if x%2==0 and x%3==0:
        y=y*x
print(y)