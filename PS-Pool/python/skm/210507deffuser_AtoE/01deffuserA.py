from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

global N,M
global matrix, willbevisited, totalvisited
global costMatrix, totalcostMatrix
global cnt_perform

def check_totalvisited():
    global totalvisited
    cnt=0
    for row in totalvisited:cnt+=sum(row)
    return cnt

def check_totalcostMatrix():
    global totalcostMatrix
    max_cost=0
    for row in totalcostMatrix:
        cand=max(row)
        if(cand>max_cost): max_cost=cand

    return max_cost

def bfs_deffuser(v):
    global N,M
    global matrix, willbevisited,totalvisited
    global costMatrix,totalcostMatrix
    
    q=deque()

    init_cost=0

    startR, startC = v
    willbevisited[startR][startC]=1
    q.append((startR,startC,init_cost))

    # setting of bfs
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    while(q):
        curR,curC,curCost = q.popleft()
        # action
        costMatrix[curR][curC]=curCost

        cost = curCost + 1
        # search of bfs
        for d in range(4):
            adjR, adjC = curR+dr[d], curC+dc[d]
            if(adjR<0 or adjR>N-1 or adjC<0 or adjC>M-1): continue
            if(matrix[adjR][adjC]==1): continue
            
            #valid adj and check willbevisited
            if(willbevisited[adjR][adjC]==1): continue
            else:
                willbevisited[adjR][adjC]=1
                q.append((adjR,adjC,cost))

    # update total, final
    for r in range(N):
        for c in range(M):
            if(totalvisited[r][c]==0): totalvisited[r][c]= willbevisited[r][c]
            
            if(willbevisited[r][c]==1):
                if(totalcostMatrix[r][c]==''): totalcostMatrix[r][c]=costMatrix[r][c]
                else:
                    if(costMatrix[r][c]<totalcostMatrix[r][c]): totalcostMatrix[r][c]=costMatrix[r][c] 

if __name__=="__main__":
    N,M= map(int,input().split())

    matrix=[list(map(int,input().split())) for _ in range(N)]
    # print(*matrix, sep='\n')
    totalcostMatrix=[['']*M for _ in range(N)]
    totalvisited=[[0]*M for _ in range(N)]
    # Deffuser Number : COORD   
    DN_COORD = {}
    num=1
    # target cnt of room to make perfect deffuse
    cnt_targetroom=0
    # r,c  INDEX OF COMPUTER
    for r in range(N):
        for c in range(M):
            if(matrix[r][c]==2):
                DN_COORD[num]=(r,c)
                num+=1

                cnt_targetroom+=1
            elif(matrix[r][c]==0): cnt_targetroom+=1

            elif(matrix[r][c]==1): totalcostMatrix[r][c]=-1
    # print(DN_COORD)

    Deffusers=DN_COORD.keys()
    # print(Deffusers)

    # combi=list(combinations(Deffusers,K))
    # print(combi)

    # for component in combi[T-1]:
    #     r,c=DN_COORD[component]
    #     print(r+1,c+1)


    for DN in Deffusers:
        # setting of bfs
        willbevisited=[[0]*M for _ in range(N)]
        costMatrix=[[0]*M for _ in range(N)]
        bfs_deffuser(DN_COORD[DN])
        
        # print(*costMatrix,sep='\n')
        # print('--')
        
        # print(*willbevisited,sep='\n')
        # print('--')

    # check the total result of multi bfs
    cnt_perform=check_totalvisited()
    
    # print('------')

    # print(*totalvisited,sep='\n')
    # print('--')
    # print(*totalcostMatrix,sep='\n')
    # print('--')
    
    # print(cnt_perform, cnt_targetroom)
    if(cnt_perform==cnt_targetroom):
        max_cost=check_totalcostMatrix()
        print(max_cost)
    else:
        print(-1)