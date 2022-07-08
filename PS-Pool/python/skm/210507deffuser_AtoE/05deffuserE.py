from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

global N,M
global matrix, willbevisited, totalvisited
global costMatrix, totalcostMatrix
global EffectedMatrix

def check_EffectedMatrix():
    global N,M
    global totalvisited
    global EffectedMatrix

    for r in range(N):
        for c in range(M):
            if(totalvisited[r][c]==1 or matrix[r][c]==2):
                EffectedMatrix[r][c]=1
    cnt=0
    for row in EffectedMatrix:
        cnt+=sum(row)
    
    return cnt

def check_totalcostMatrix():
    global N,M
    global totalcostMatrix
    max_cost=0

    for r in range(N):
        for c in range(M):
            if(totalcostMatrix[r][c]!=''):
                if(totalcostMatrix[r][c]>max_cost): max_cost=totalcostMatrix[r][c]
            else: pass

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
        # adjust cost of deffuse already
        if(matrix[curR][curC]==2): costMatrix[curR][curC]=0

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
            # update total visit if current willbevisited is 1 and
            # update total cost in case of visited
            if(willbevisited[r][c]==1): 
                totalvisited[r][c]= 1
           
                if(totalcostMatrix[r][c]==''): totalcostMatrix[r][c]=costMatrix[r][c]
                else:
                    if(costMatrix[r][c]<totalcostMatrix[r][c]): totalcostMatrix[r][c]=costMatrix[r][c] 
            # if barrier, update costMatrix for rear process
            if(matrix[r][c]==1): totalcostMatrix[r][c]=-1

if __name__=="__main__":
    T = int(input().strip())
    
    results=[]
    for idxT in range(1,T+1):
        N,M,K= map(int,input().split())
        matrix=[list(map(int,input().split())) for _ in range(N)]
        # print(*matrix, sep='\n')
    
        COORDs=[]
        # target cnt of room to make perfect deffuse
        cnt_targetroom=0
        # r,c  INDEX OF COMPUTER
        for r in range(N):
            for c in range(M):
                if(matrix[r][c]!=1):
                    cnt_targetroom+=1
                    if(matrix[r][c]==2): COORDs.append((r,c))
                else: pass
        # Deffuser Number : COORD of deffuser  
        nums=[i for i in range(1,len(COORDs)+1)]
        DN_COORD=dict(zip(nums,COORDs))
        Deffusers=DN_COORD.keys()
        # print(DN_COORD)

        combi=list(combinations(Deffusers,K))
        # print(combi)

        results_testcase=[]
        for testcase in combi:
            # re init per testcase ; (1,)
            totalvisited=[[0]*M for _ in range(N)]
            totalcostMatrix=[['']*M for _ in range(N)]
            EffectedMatrix=[[0]*M for _ in range(N)]
            cnt_Effected=0

            for DN in testcase:
                # setting of bfs per bfs
                willbevisited=[[0]*M for _ in range(N)]
                costMatrix=[[0]*M for _ in range(N)]
                bfs_deffuser(DN_COORD[DN])
                
                # print(*costMatrix,sep='\n')
                # print('-')
                # print(*willbevisited,sep='\n')
                # print('--')

            # check the total result of multi bfs
            cnt_Effected=check_EffectedMatrix()
            
            # print('------')
            # print(*totalcostMatrix,sep='\n')
            # print('--')
            # print(*totalvisited,sep='\n')
            # print('--')

            # print(cnt_Effected, cnt_targetroom)
            if(cnt_Effected==cnt_targetroom):
                max_cost=check_totalcostMatrix()
                # print(max_cost)
                results_testcase.append(max_cost)
            else:
                # print(-1)
                results_testcase.append(-1)
        
        # print('ck',results_testcase)
        allminusToken=True
        best_time=10000
        for item in results_testcase:
            if(item==-1): pass
            else:
                allminusToken=False
                if(item<best_time): best_time=item
        
        if(allminusToken):
            # print(-1)
            results.append(-1)
        else: 
            # print(best_time)
            results.append(best_time)
    
    print(results)