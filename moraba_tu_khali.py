andaze = int(input())

for i in range(1,andaze+1):
    for j in range(1,andaze+1):
        if i == 1 or j == 1 or i==andaze or j==andaze :
            print("*", end="")
        else:
            print(" ",end="")
    print()