# 수영장청소 C
# 오후 10:24 2021-05-11
# core contents ; consecutive move of BFS; bfs variation
# step of Main
# 1. input and numbering the fauset and record the COORD to find certain fauset
# !! First, by using deque casting and independent deque.rotate def deal with cycle, and then using the OpenFauset def

# 2. cleaned area by circular fauset 
# !! indexing the 4way direction as a standard and expansion with 4way operation of faucet which has 5 kinds of operation

# description of problem
# bfs with 2d matrix, circular fauset, which have feature per direction

import sys
input=sys.stdin.readline
from itertools import product
from collections import deque

global N,M,K,T
global matrix
global COORD_fauset
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
def openFauset(r,c,T):
    global N,M
    global matrix
    stdR, stdC = r,c
    faucetNum=matrix[stdR][stdC]

    availables=faucetkind_possibleDir[faucetNum]
    rotated_avails=rotate_possibledir(availables,T)
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

if __name__=="__main__":
    #step 1
    N,M,K,T=map(int,input().split())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    # print(*matrix,sep='\n')
    orderNum=1
    faucetNum_COORD={}
    for r in range(N):
        for c in range(M):
            if(1<=matrix[r][c] and matrix[r][c]<=5):
                faucetNum_COORD[orderNum]=(r,c)
                orderNum+=1
    # print(faucetNum_COORD)

    # step 2
    stdR, stdC = faucetNum_COORD[K]
    openFauset(stdR,stdC,T)
    # print(*matrix, sep='\n')
    cnt_cleaned=0
    for r in range(N):
        for c in range(M):
            if(matrix[r][c]==8): cnt_cleaned+=1
    
    print(cnt_cleaned)