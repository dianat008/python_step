lis_t = input().split()
p=lis_t[0]
d=lis_t[1]
p = int(p)
d = int(d)
if p>=2 and p<=100 and d>=1 and d<=1000 :
    for i in range(1, 51):
        mazrab = i*d
        mohasebe = mazrab%p
        if mohasebe>=0 and mohasebe<=(p/2):
            print(mazrab)
            break

        else:
            continue