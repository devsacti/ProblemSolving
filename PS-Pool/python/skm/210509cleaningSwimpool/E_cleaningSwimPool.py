# 수영장청소 E
# 오전 11:46 2021-05-12
# core contents ; consecutive move of BFS; bfs variation
# step of Main
# 1. input and numbering the fauset and record the COORD to find certain fauset
# 2. cleaned area by circular fauset 
# !! indexing the 4way direction as a standard and expansion with 4way operation of faucet which has 5 kinds of operation

# description of problem
# bfs with 2d matrix, circular fauset, which have feature per direction
# for문이 많아지니까 너무 초기화 문제와 분할이 쉽지 않음, 최대한 문맥에 맞게 쪼개고,
# 초기화 for구조에 익숙해져야
import sys
input=sys.stdin.readline
from itertools import product
from collections import deque

global N,M
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
def openFauset(FausetNum):
    global N,M
    global matrix
    # preserve
    stdR, stdC=faucetNum_COORD[FausetNum]
    faucetkind=matrix[stdR][stdC]
    # print('cur',FausetNum,'/',stdR,stdC,'/',faucetkind)

    availables=faucetkind_possibleDir[faucetkind]
    max_cnt=0
    for T in [0,1,2,3]:
        rotated_avails=rotate_possibledir(availables,T)
        # print('from',availables,'to',rotated_avails)
        # print('--')
        testMatrix=[]
        for row in matrix:
            testMatrix.append(row[:])
        # print(*testMatrix,sep='\n')
        # print('-before spread-')
        
        # basic idea is  0 1 2 3 <=> kinds of direction(clockwise)
        BasicStandard=[0,1,2,3]
        # based on basic idea, component version of direction vector
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]

        for d in BasicStandard:
            #reiniit
            r,c=stdR, stdC
            # print('ck',r,c)
            if(rotated_avails[d]):
                while(1):
                    candR,candC = r+dr[d],c+dc[d] 

                    if(candR<0 or candR>(N-1) or candC<0 or candC>(M-1)): break
                    if(testMatrix[candR][candC]==6): break

                    # arrival at 0
                    if(1<=testMatrix[candR][candC]<=5): pass
                    else: testMatrix[candR][candC]=8
                    r,c = candR,candC
            else: continue
        print(*testMatrix,sep='\n')
        print('--')
        
        cnt_cleaned=0
        for r in range(N):
            for c in range(M):
                if(testMatrix[r][c]==8): cnt_cleaned+=1
        
        if(cnt_cleaned>max_cnt): 
            max_cnt=cnt_cleaned
            # print('ck', max_cnt)
    
    return max_cnt

if __name__=="__main__":
    #step 1
    N,M=map(int,input().split())
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
    maxCnt_perFauset=0
    for key in faucetNum_COORD:
        cand=openFauset(key)
        # print(*matrix, sep='\n')
        if(cand>maxCnt_perFauset):maxCnt_perFauset=cand
    
    print(maxCnt_perFauset)