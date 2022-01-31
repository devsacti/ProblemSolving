# 수영장청소 final
# 오후 3:34 2021-05-12
# core contents ; consecutive move of BFS; bfs variation, with itertools.product
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
def openFauset(experiMatrix,FausetNum,rotateCNT):
    global N,M
    # preserve
    stdR, stdC=faucetNum_COORD[FausetNum]
    faucetkind=experiMatrix[stdR][stdC]
    # print('cur',FausetNum,'/',stdR,stdC,'/',faucetkind)

    availables=faucetkind_possibleDir[faucetkind]
    rotated_avails=rotate_possibledir(availables,rotateCNT)

    # basic idea is  0 1 2 3 <=> kinds of direction(clockwise)
    BasicStandard=[0,1,2,3]
    # based on basic idea, component version of direction vector
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]

    cnt_cleaned=0
    for d in BasicStandard:
        #reiniit
        r,c=stdR, stdC
        # print('ck',r,c)
        if(rotated_avails[d]):
            while(1):
                candR,candC = r+dr[d],c+dc[d] 

                if(candR<0 or candR>(N-1) or candC<0 or candC>(M-1)): break
                if(experiMatrix[candR][candC]==6): break

                # arrival at 0
                if(1<=experiMatrix[candR][candC]<=5): pass
                elif(experiMatrix[candR][candC]==0): 
                    experiMatrix[candR][candC]=8
                    cnt_cleaned+=1

                r,c = candR,candC
        else: continue
    # print(*experiMatrix, sep='\n')
    # print('--')
    return cnt_cleaned
        
if __name__=="__main__":
    #step 1
    T=int(input().strip())

    resultsTestcase=[]
    for idxt in range(1,T+1):
        N,M=map(int,input().split())
        matrix=[list(map(int, input().split())) for _ in range(N)]
        # print(*matrix,sep='\n')

        cnt_faucet=0
        cnt_obstacle=0
        cnt_extra=0

        orderNum=1
        faucetNum_COORD={}
        for r in range(N):
            for c in range(M):
                if(1<=matrix[r][c] and matrix[r][c]<=5):
                    faucetNum_COORD[orderNum]=(r,c);orderNum+=1
                    cnt_faucet+=1
                elif(matrix[r][c]==6): cnt_obstacle+=1
                else: cnt_extra+=1
        
        # print(faucetNum_COORD)
        # make bruteforce cases of rotate of faucet, with 1 start indexing 
        cases=list(product(range(4),repeat=cnt_faucet))
        # print(cases)

        # step 2 ; step into testmMatrix
        # results=[]
        minResult=10000000
        for case in cases:
            # init of for
            # print('--per case--')
            experiMatrix=[]
            for row in matrix: experiMatrix.append(row[:])
            # act of for
            val_case=0
            for key in faucetNum_COORD:
                val=openFauset(experiMatrix,key,case[key-1])
                val_case+=val
            
            val_left=cnt_extra-val_case
            # results.append(val_left)
            if(val_left<minResult): minResult=val_left

        # print(minResult)
        resultsTestcase.append((idxt,minResult))
    
    for item in resultsTestcase:
        print('#'+str(item[0]), item[1])