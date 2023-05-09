def code_cup():
    dama = int(input())
    if dama<0 and dama>= -273:
        print("Ice")

    elif dama>=0 and dama<=100:
        print("Water")

    elif dama>100 and dama<=6000:
        print("Steam")

    else:
        print(" ")


code_cup()