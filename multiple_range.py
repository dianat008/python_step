vorudy = int(input())
if vorudy>=1 and vorudy<=100:
    vorudy = vorudy+1
    for peymayesh_gar in range(1, vorudy): 
        for zarb_n_ha in range(1, vorudy):
            print(peymayesh_gar * zarb_n_ha, end=' ')
        print()
else:
    print(' ')