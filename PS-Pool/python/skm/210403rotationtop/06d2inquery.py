#2차원 조회

import sys

def checkeradjacent(idx_r,idx_c):
    global matrix,checkmatrix

    kinds_direction=4
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    
    token_same=False
    for d in range(kinds_direction):
        cand_idx_r=idx_r+dr[d]
        cand_idx_c=idx_c+dc[d]

        if(cand_idx_r<0 or cand_idx_r>n-1):
            continue

        if(cand_idx_c<0 or cand_idx_c>m-1):
            cand_idx_c=(cand_idx_c+m)%m
        
        # print('trial ',idx_r,idx_c,cand_idx_r,cand_idx_c)
        if(matrix[idx_r][idx_c]==matrix[cand_idx_r][cand_idx_c]):
            token_same=True
        
    if(token_same):
        checkmatrix[idx_r][idx_c]='1'

if __name__=="__main__":
    n,m =map(int,sys.stdin.readline().split())

    matrix=[]
    for _ in range(n):
        row=sys.stdin.readline().split()
        matrix.append(row)
    # print(*matrix,sep='\n')

    checkmatrix=[['0']*m for _ in range(n)]

    for idx_r in range(n):
        for idx_c in range(m):
            checkeradjacent(idx_r,idx_c)

    # print()
    # print(*checkmatrix,sep='\n')
    for row in checkmatrix:
        print(' '.join(row))