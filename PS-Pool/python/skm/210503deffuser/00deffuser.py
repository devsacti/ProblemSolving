# 디퓨져
# 오전 12:42 2021-05-04
# type ; bfs , combination
# steps of main
# step 1 ; input and make combination
# step 2 ; bfs and find min between maxCost of bfs in case of perfecdiffuse
# step 2.5 ; judge allminusone and find valid min 

# tcp 1: totalvisited 기반으로 check perfectdiffuse를 판별하는데, visited와 향기에 의한 effect는 다른 개념이고, 불일치로 오류
# 1
# 3 3 1
# 2 0 0
# 0 1 1
# 1 2 2 
# sol.bfs의 기본변수로 풀려고하지말고, 문제용 하나 반드시 추가

import sys
from collections import deque
from itertools import combinations

global N,M,K
global matrix,effectedMatrix
global willbevisited, totalwillbevisited
global deffuser_COORD
global maxCost

def bfs_deffuser(v):
    global N,M
    global matrix, effectedMatrix
    global willbevisited, totalwillbevisited,costMatrix
    global maxCost
    q=deque()
    cost=0
    q.append((v[0],v[1],cost))

    while(q):
        curR, curC, curCost = q.popleft()
        # print(curR,curC)
        effectedMatrix[curR][curC]=1
        
        totalwillbevisited[curR][curC]=1
        willbevisited[curR][curC]=1

        # 초기 상태면 일단 할당, 초기상태 아니면 비교 후 대입
        if(costMatrix[curR][curC]==' '):
            costMatrix[curR][curC]=curCost
        else:
            if(curCost<costMatrix[curR][curC]):
                costMatrix[curR][curC]=curCost

        # if place of deffuser, renew cost as 0
        if(matrix[curR][curC]==2):
            effectedMatrix[curR][curC]=1
            costMatrix[curR][curC]=0

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

def findMaxCost():
    global N,M
    global costMatrix
    
    wanted=-1

    for r in range(N):
        for c in range(M):
            if(costMatrix[r][c]==' '): pass
            elif(costMatrix[r][c]>wanted): wanted=costMatrix[r][c]

    return wanted

def check_PerfectDiffuse():
    global N,M
    global matrix,effectedMatrix
    global totalwillbevisited
    global deffuser_COORD

    token_perfectdiffuse=True

    # update the basic effect of deffuser place
    for coord in deffuser_COORD.values():
        r,c=coord
        effectedMatrix[r][c]=1

    for r in range(N):
        for c in range(M):
            if(effectedMatrix[r][c]==0 and matrix[r][c] !=1):
                token_perfectdiffuse=False

    return token_perfectdiffuse

if __name__=="__main__":
    T = int(sys.stdin.readline().strip())

    resultTestcase=[]
    for label in range(1,T+1):
        # step 1
        N,M,K = map(int, sys.stdin.readline().split())

        deffuser_COORD={}
        orderNum=1

        ##!!!!! 문제 맞춤형 변수 필수추가, 모든 combi에서 공통
        # effectedMatrix=[[0]*M for _ in range(N)]

        matrix=[]
        # 시간 소요 감축 전략 상 여기서 check wheter all places are diffuser
        token_alldiffuser=True
        # r,c ; INDEX OF COMPUTER
        for r in range(N):
            row = list(map(int, sys.stdin.readline().split()))
            for c, item in enumerate(row):
                if(item == 2):
                    deffuser_COORD[orderNum]=(r,c)
                    orderNum+=1
                    
                    # update basic effect by place of deffuser
                    # effectedMatrix[r][c]=1
                    # for문의 복잡한 범위 문제로 check perfect diffuse에서 좌표이용 업데이트하기로 결정
                else:
                    token_alldiffuser=False
            matrix.append(row)
        # print(deffuser_COORD)
        # print(token_alldiffuser)
        
        # step 2
        maxCost_list=list()
        if(token_alldiffuser):
            maxCost=0
            maxCost_list.append(maxCost)
        else:
            samples=[i for i in range(1,orderNum)] 
            combi_li=list(combinations(samples, K))
            # print(combi_li)
            
            for combi in combi_li:
                # custum
                effectedMatrix=[[0]*M for _ in range(N)]

                # bfs setting per combi
                # print('cur combi', combi)
                totalwillbevisited=[[0]*M for _ in range(N)]
                costMatrix=[[' ']*M for _ in range(N)]
                maxCost=0

                for deffuserNum in combi:
                    # reinit per bfs
                    willbevisited=[[0]*M for _ in range(N)]
                    # bfs
                    bfs_deffuser(deffuser_COORD[deffuserNum])
                
                # print('---')
                # for row in costMatrix: print(' '.join(map(str,row)))
                # print(*willbevisited,sep='\n')
                # print('--')
                # print(*effectedMatrix,sep='\n')

                # check perfectdiffuse                
                # find max at costmatirx, after K times bfs
                # print(check_PerfectDiffuse())
                if(check_PerfectDiffuse()):
                    maxCost=findMaxCost()
                else:
                    maxCost=-1
                # print(maxCost)
                maxCost_list.append(maxCost)

        # print(maxCost_list)
            
        # find valid cost, except -1 in maxCost list
        allminusone=True
        validmin=1000000
        for item in maxCost_list:
            if(item==-1): pass # allminus val is maintained
            else:
                allminusone=False
                if(item<validmin):
                    validmin=item

        if(allminusone): resultTestcase.append((label,-1))
        else:resultTestcase.append((label,validmin))
        # after checking all combi, find best; min of maxcost
    
    # print(resultTestcase)
    for result in resultTestcase:
        print('#'+str(result[0]),result[1])