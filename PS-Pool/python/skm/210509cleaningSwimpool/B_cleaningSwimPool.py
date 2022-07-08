# 수영장청소 B
# 오후 4:19 2021-05-10
# core contents ; consecutive move of BFS; bfs variation
# step of Main
# 1. input
# 2. cleaner 
# !! there are commonly 4 ways of water direction of faucet, it is very important common feature of five faucet
# so by making token per way of water direction, we can handle all fauset
# for example,
# 1th faucet; up : open(=1), down : closed(=0), left : closed, right : closed
# 5th faucet; up : 1, down : 1 blabla
# finallay, like basic bfs, spread 4ways(0~3) 
# and plus, chech the open or close
# and if open, by using while, go to limit or obstacle
# the most big difference with basic bfs is consecutive move(0~tolimit) per direction, basic bfs is move only 1 per 1 way
import sys
input=sys.stdin.readline
from itertools import product

global N,M
global matrix
global COORD_fauset
global faucet_possibleDir
faucet_possibleDir={
    # faucet number : indexed direction ; up, down, left, right => 0 1 2 3
    #   0 1 2 3
    1: [1,0,0,0],
    2: [1,1,0,0],
    3: [1,0,0,1],
    4: [1,0,1,1],
    5: [1,1,1,1]
}

# BFS
def openFauset(r,c):
    global N,M
    global matrix
    stdR, stdC = r,c
    faucetNum=matrix[stdR][stdC]
    availables=faucet_possibleDir[faucetNum]
    # basic idea is  0 1 2 3 <=> kinds of direction(up,down, left,right)
    BasicStandard=[0,1,2,3]
    # based on basic idea, component version of direction vector
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    for d in BasicStandard:
        #reiniit
        stdR, stdC = r,c
        if(availables[d]):
            while(1):
                candR,candC = stdR+dr[d],stdC+dc[d] 

                if(candR<0 or candR>(N-1) or candC<0 or candC>(M-1)): break
                if(matrix[candR][candC]==6): break

                # arrival at 0
                matrix[candR][candC]=8
                stdR,stdC = candR,candC
        else: continue

if __name__=="__main__":
    N,M=map(int,input().split())

    matrix=[list(map(int, input().split())) for _ in range(N)]
    # print(*matrix,sep='\n')

    COORD_fauset={}
    for r in range(N):
        for c in range(M):
            if(1<=matrix[r][c] and matrix[r][c]<=5):openFauset(r,c)
    
    # print(*matrix, sep='\n')
    for row in matrix: print(' '.join(map(str,row)))