# 조합 알고리즘 2
# 오후 5:18 2021-05-03
# type : itertools product
# summary
# 
import sys
from itertools import combinations

if __name__=="__main__":
    N,M ,K,T = map(int, sys.stdin.readline().split())
    
    matrix=[]
    coord_diffuser={}
    diffuser_coord={}
    orderNum=1

    for r in range(1,N+1):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

        for c,item in enumerate(row,1):
            if(item == 2):
               coord_diffuser[(r,c)]=orderNum
               orderNum+=1

    diffuser_coord={v : k for k,v in coord_diffuser.items()}

    # print(coord_diffuser)
    # print(diffuser_coord)    

    diffusers=diffuser_coord.keys()

    for diffuser in list(combinations(diffusers, K))[T-1]:
        r,c=diffuser_coord[diffuser]
        print(r,c)
