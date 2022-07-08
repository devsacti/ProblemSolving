# 확산 알고리즘 2
# 오후 7:37 2021-05-03
# type : itertools product
# summary
# 
import sys
from collections import deque

# tcp 1 ; accuracy; deffuser place is already cleaned, so dont count time
# but considering adj of deffuser are still updated, so after all costmatrix is updated
# only the place of deffuser is updated as 0

# tcp2 ; all bfs is -1 but if all left place of matrix is deffuser, this case cost is 0 not -1
# 2 1
# 1 2
# 각 디퓨져는 벽에 갇혀있고 어느쪽에서 bfs하든 완전확산불가이나, 애당초 모두 cost가 0로 pass
# 이런 기능을 check_perfectdiffuse에 추가할수 있고,
# 만약 모든 남은 칸이 디퓨져면 이동 가능성도 없고
# costMatrix의 maxCost가 정의가 되는데, 모두 다 0이라 max가 0인 특징을 이용해서 별도 판단

global N,M
global matrix, willbevisited, totalwillbevisited,costMatrix
global maxCost

def findMaxCost():
    global N,M
    global costMatrix
    global maxCost

    for r in range(N):
        for c in range(M):
            if(costMatrix[r][c]==' '): pass
            elif(costMatrix[r][c]>maxCost):
                maxCost=costMatrix[r][c]

def check_PerfectDiffuse():
    # global matrix,totalwillbevisited
    # as a sub module, in this time, handle willbevisited not total~
    global matrix, willbevisited

    token_perfectdiffuse=True
    for r,row in enumerate(willbevisited):
        for c, item in enumerate(row):
            if(item == 0 and matrix[r][c] !=1):
                token_perfectdiffuse=False

    return token_perfectdiffuse

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
    N,M= map(int, sys.stdin.readline().split())
    
    matrix=[]
    coord_diffuser={}
    diffuser_coord={}
    orderNum=1

    # r,c INDEX OF COMPUTER
    for r in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

        for c,item in enumerate(row):
            if(item == 2):
               coord_diffuser[(r,c)]=orderNum
               orderNum+=1

    diffuser_coord={v : k for k,v in coord_diffuser.items()}
    # print(coord_diffuser)
    # print(diffuser_coord)    

    diffusers=diffuser_coord.keys()

    # bfs setting
    totalwillbevisited=[[0]*M for _ in range(N)]

    costs_BFS=[]
    for diffuser in diffusers:
        costMatrix=[[' ']*M for _ in range(N)]
        willbevisited=[[0]*M for _ in range(N)]
        maxCost=0
    
        bfs_deffuser(diffuser_coord[diffuser])

        # the place of deffuser is updated as 0
        for diffuser in diffusers:
            r,c=diffuser_coord[diffuser]
            costMatrix[r][c]=0
        
        # print('--')
        # for row in costMatrix: print(' '.join(map(str,row)))
        # print('-')
        # print(*willbevisited, sep='\n')
        # print('-----')
        #maxCost is definited by findMaxCost()
        findMaxCost()
        # print(maxCost)

        if(check_PerfectDiffuse() or maxCost ==0): costs_BFS.append(maxCost)
        else: costs_BFS.append(-1)
        # print(costs_BFS)

    minCost_BetweenBFS=10000000
    allfail=True
    for result in costs_BFS:
        if(result == -1): continue
        else:
            if(result<minCost_BetweenBFS): minCost_BetweenBFS=result
            allfail=False

    if(allfail): print(-1)
    else: print(minCost_BetweenBFS)
