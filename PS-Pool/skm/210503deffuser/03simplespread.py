# 단순 확산
# 오후 4:10 2021-05-03
# type : bfs
# summary
# willbevisited와 매트릭스로 벽이 아님에도 확산되지 않음을 판별하여 전체확산 판별
# 전체확산 가능하다면, bfs가 가졌된 최대 비용을 따로 저장하여 출력

# tcp 1 ; !!! 벽이면 -1 할당을 통해서 willbevisted로 전체확산 여부를 판단했는데
# 만약 벽이 이중이면 벽이라서 어짜피 안들어가도 되는데 벽에 둘러싸인 벽의 willbevisited가
# 0으로 남아서 오류!!! 어찌 발견한거지 난..
import sys
from collections import deque

global N,M
global matrix, willbevisited, costMatrix
global maxCost

def check_PerfectDiffuse():
    global matrix,willbevisited

    for r,row in enumerate(willbevisited):
        for c, item in enumerate(row):
            if(item == 0 and matrix[r][c] !=1):
                return 0
    return 1

def bfs_deffuer(v):
    global N,M
    global matrix, willbevisited, costMatrix
    global maxCost
    q=deque()
    cost=0
    q.append((v[0],v[1],cost))
    maxCost=0

    while(q):
        curR, curC, curCost = q.popleft()
        # print(curR,curC)
        willbevisited[curR][curC]=1
        costMatrix[curR][curC]=curCost
        if(curCost>maxCost):
            maxCost=curCost

        dr=[1,-1,0,0]
        dc=[0,0,1,-1]

        cost=curCost+1
        for d in range(4):
            adjR=curR+dr[d]
            adjC=curC+dc[d]

            if(adjR<0 or adjR>(N-1) or adjC<0 or adjC>(M-1)): continue

            if(matrix[adjR][adjC]==1):
                willbevisited[adjR][adjC]=-1
                continue

            if(willbevisited[adjR][adjC]==1): continue
            else:
                willbevisited[adjR][adjC]=1
                q.append((adjR,adjC,cost))

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())
    
    matrix=[]
    for r in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

        for c,item in enumerate(row):
            if(item == 2):
                start = (r,c)
    
    willbevisited=[[0]*M for _ in range(N)]
    costMatrix=[[0]*M for _ in range(N)]
    
    maxCost=0
    bfs_deffuer(start)

    # print(*willbevisited, sep='\n')
    # print(*costMatrix, sep='\n')
    # print(maxCost)

    if(check_PerfectDiffuse()):
        print(maxCost)
    else:
        print(-1)
