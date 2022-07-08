# 2개 확산
# 오후 5:18 2021-05-03
# type : bfs
# summary
# willbevisited와 매트릭스로 벽이 아님에도 확산되지 않음을 판별하여 전체확산 판별
# 전체확산 가능하다면, bfs가 가졌된 최대 비용을 따로 저장하여 출력

# lesson 1 ; 1개의 costmatrix에 대해서 2개가 작동하는데, 최소값으로 갱신시켜라!
# 처음에는 목수의 미로탈출 풀었을 때처럼 2개씩 선언했는데, 최소값 갱신 방법으로 1개에 대해서 처리하면
# 2개의 비용매트릭스에 대해서 추후 좌표별 최소값을 갱신과정 간소화가능
# 무엇보다 목수의 미로탈출도 이렇게 가능할듯, 

# tcp 1 ; 만약 격리된 두 공간에 각각 디퓨져가 있는 경우, 한쪽 bfs의 willbevisited만 남아서 문제발생
# Sol) <F> 공통 visited를 쓰되, 2번까지 방문 허용하고 나중에 1,2인 경우 제외해서 완전방문 판단
# 이렇게 하면 기본적으론 1개 bfs내에서도 서로 다른 접근으로 같은 좌표 방문시 비용이 잘못갱신됨
# sol) 종합 visited를 만들자.

import sys
from collections import deque

global N,M
global matrix, willbevisited, totalwillbevisited,costMatrix
global maxCost

# renewed costmatrix by two bfs, each maxcost of bfs is not valid
# so we neeed new function
def findMaxCost():
    global N,M
    global costMatrix
    global maxCost

    maxCost=0
    for r in range(N):
        for c in range(M):
            if(costMatrix[r][c]==' '): pass
            elif(costMatrix[r][c]>maxCost):
                maxCost=costMatrix[r][c]

def check_PerfectDiffuse():
    global matrix,totalwillbevisited

    for r,row in enumerate(totalwillbevisited):
        for c, item in enumerate(row):
            if(item == 0 and matrix[r][c] !=1):
                return 0
    return 1

def bfs_deffuser(v):
    global N,M
    global matrix, willbevisited, totalwillbevisited,costMatrix
    global maxCost
    q=deque()
    cost=0
    q.append((v[0],v[1],cost))

    while(q):
        curR, curC, curCost = q.popleft()
        # print(curR,curC)
        totalwillbevisited[curR][curC]=1
        willbevisited[curR][curC]=1

        # 초기 상태면 일단 할당, 초기상태 아니면 비교 후 대입
        if(costMatrix[curR][curC]==' '):
            costMatrix[curR][curC]=curCost
        else:
            if(curCost<costMatrix[curR][curC]):
                costMatrix[curR][curC]=curCost

        dr=[1,-1,0,0]
        dc=[0,0,1,-1]

        cost=curCost+1
        for d in range(4):
            adjR=curR+dr[d]
            adjC=curC+dc[d]

            if(adjR<0 or adjR>(N-1) or adjC<0 or adjC>(M-1)): continue

            if(matrix[adjR][adjC]==1): continue

            if(willbevisited[adjR][adjC]==1): continue
            else:
                totalwillbevisited[adjR][adjC]=1
                willbevisited[adjR][adjC]=1
                q.append((adjR,adjC,cost))

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())
    
    matrix=[]
    coord_diffuser=[]

    for r in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

        for c,item in enumerate(row):
            if(item == 2):
               coord_diffuser.append((r,c))
    
    costMatrix=[[' ']*M for _ in range(N)]
    totalwillbevisited=[[0]*M for _ in range(N)]

    for v in coord_diffuser:
        willbevisited=[[0]*M for _ in range(N)]
        bfs_deffuser(v)
        # print(*willbevisited, sep='\n')

    # for row in costMatrix:
    #     print(' '.join(map(str,row)))

    findMaxCost()
    # print(maxCost)

    if(check_PerfectDiffuse()):
        print(maxCost)
    else:
        print(-1)
