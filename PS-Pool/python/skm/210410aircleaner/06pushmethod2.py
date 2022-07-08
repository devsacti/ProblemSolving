# 개요
# pushrobot이 돌면서 발판을 겟하고 갱신하면서 이동하고나면 로테이션이 끝나는 알고리즘

import sys
from collections import deque
# pushrobot으로 발전,
# cur 에 대해서 get set
# 1. 초기 상태면 get만
# 2. 그다음부터는 get set
# next 에 대해서 get set
# 1. next get and 들고있는 것 set

def pushrobot_up(startR, startC):
    global N,M,matrix
    global up

    # q is for waiting line of values for set
    q=deque()
    # get init value 
    q.append(matrix[startR][startC])

    # direction vectors
    magnitude=1
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    kinds_dir=len(dr)
    d=0

    curR,curC = startR, startC
    # init next
    nextR, nextC = -1, -1
    # not(startR == nextR and startC == nextC) is same with below
    while( nextR != startR or nextC != startC ):
        # next 탐색
        candR=curR+dr[d]
        candC=curC+dc[d]
        # print(candR,candC,curR,curC)

        if(candR<0 or candR>up or candC<0 or candC>M-1):
            d+=1
            candR=curR+dr[d]
            candC=curC+dc[d]
            # print('#',candR,candC,curR,curC)

        nextR, nextC = candR, candC
        q.append(matrix[nextR][nextC])

        #go to next spot
        curR, curC = nextR, nextC
        # set the value
        matrix[curR][curC] = q.popleft()

def pushrobot_down(startR, startC):
    global N,M,matrix
    global down

    # q is for waiting line of values for set
    q=deque()
    # get init value 
    q.append(matrix[startR][startC])

    # direction vectors
    magnitude=1
    dr=[-1,0,1,0]
    dc=[0,-1,0,1]
    kinds_dir=len(dr)
    d=0

    curR,curC = startR, startC
    # init next
    nextR, nextC = -1, -1
    # not(startR == nextR and startC == nextC) is same with below
    while( nextR != startR or nextC != startC ):
        # next 탐색
        candR=curR+dr[d]
        candC=curC+dc[d]
        # print(candR,candC,curR,curC)

        if(candR<down or candR>N-1 or candC<0 or candC>M-1):
            d+=1
            candR=curR+dr[d]
            candC=curC+dc[d]
            # print('#',candR,candC,curR,curC)

        nextR, nextC = candR, candC
        q.append(matrix[nextR][nextC])

        #go to next spot
        curR, curC = nextR, nextC
        # set the value
        matrix[curR][curC] = q.popleft()

if __name__=="__main__":
    global N,M
    N,M = map(int, sys.stdin.readline().split())

    global matrix
    matrix=[]
    for _ in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    global up,down
    up,down= map(int, sys.stdin.readline().split())

    pushrobot_up(0,0)
    pushrobot_down(N-1,M-1)

    # print(*matrix,sep='\n')
    for row in matrix:
        print(' '.join(map(str,row)))