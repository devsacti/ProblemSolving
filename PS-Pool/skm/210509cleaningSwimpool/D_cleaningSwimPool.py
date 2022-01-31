# 수영장청소 D

import sys
input=sys.stdin.readline
from itertools import product
from collections import deque

global N,M,K,T
global matrix
global faucetNum_COORD, faucetkind_possibleDir

def rotate_possibledir(defaultlist, T):
    rotated=deque(defaultlist)
    rotated.rotate(T)
    rotated=list(rotated)
    return rotated

faucetkind_possibleDir={
    # faucet number : indexed direction(clockwise) ; up,right, down, right => 0 1 2 3
    #   0 1 2 3
    1: [1,0,0,0],
    2: [1,0,1,0],
    3: [1,1,0,0],
    4: [1,1,0,1],
    5: [1,1,1,1]
}

# BFS
def openFauset(stdR, stdC,T):
    global N,M
    global matrix
    # preserve
    r,c=stdR, stdC
    faucetNum=matrix[stdR][stdC]
    # print('cur',stdR,stdC,faucetNum)

    availables=faucetkind_possibleDir[faucetNum]
    rotated_avails=rotate_possibledir(availables,T)
    # print('from',availables,'to',rotated_avails)
    # print('--')
    # basic idea is  0 1 2 3 <=> kinds of direction(clockwise)
    BasicStandard=[0,1,2,3]
    # based on basic idea, component version of direction vector
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]

    for d in BasicStandard:
        #reiniit
        stdR, stdC = r,c
        if(rotated_avails[d]):
            while(1):
                candR,candC = stdR+dr[d],stdC+dc[d] 

                if(candR<0 or candR>(N-1) or candC<0 or candC>(M-1)): break
                if(matrix[candR][candC]==6): break

                # arrival at 0
                if(1<=matrix[candR][candC]<=5): pass
                else: matrix[candR][candC]=8
                stdR,stdC = candR,candC
        else: continue
    # print(*matrix,sep='\n')

if __name__=="__main__":
    #step 1
    N,M=map(int,input().split())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    rotateCount=[0]+list(map(int, input().split()))
    # print(*matrix,sep='\n')
    # print(rotateCount)
    orderNum=1
    faucetNum_COORD={}
    for r in range(N):
        for c in range(M):
            if(1<=matrix[r][c] and matrix[r][c]<=5):
                faucetNum_COORD[orderNum]=(r,c)
                orderNum+=1
    # print(faucetNum_COORD)

    # step 2
    for key in faucetNum_COORD:
        stdR, stdC = faucetNum_COORD[key]
        openFauset(stdR,stdC,rotateCount[key])
    # print(*matrix, sep='\n')
    # print('--')
    cnt_cleaned=0
    for r in range(N):
        for c in range(M):
            if(matrix[r][c]==8): cnt_cleaned+=1
    
    print(cnt_cleaned)