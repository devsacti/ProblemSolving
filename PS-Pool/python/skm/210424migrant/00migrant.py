# 철새
# 오후 9:19 2021-04-28
# 교훈, 별도의 시각점 검증체계_showmatrix_를 따로 만드는데, 낯설어하지 말자.


# tcp 1
#  입력 시에는 처음부터 철새가 나무 사이 혹은 나무와 경계 사이에 놓이는 일이 없지만, 
# 다른 철새와 만나서 별 희귀한 곳으로 기어들어가면, 특정 철새에 의해서는 이동이 없는 현상 발생
# 가령 좌우로만 이동하는 철새가 다른 철새에 의해 좌우가 가로막힌 곳에 들어가면 정지이다.
# 방향 전환문제는 bfs처럼 좀더 포괄적으로 코딩해야

import sys
from collections import deque

global N,K,matirx
global COORD_Migrant,Migrant_COORD,Migrant_Dir

def move(num,cur,d):
    global N,matirx
    global Migrant_Dir

    curR, curC = cur

    # direction vector, m is magnitude
    m = 1
    dy=[-m,m,0,0]
    dx=[0,0,-m,m]
    
    # due to move of group,
    # check two direction; first, given dir, second, other dir
    # if two direction all blocked stop
    if(d==0): ds=[0,1]
    elif(d==1): ds=[1,0]
    elif(d==2): ds=[2,3]
    else: ds=[3,2]

    FrontEnd=deque()
    for d in ds:
        candR= curR + dy[d]
        candC= curC + dx[d]

        # out of range
        if(candR<0 or candR>(N-1) or candC<0 or candC>(N-1)):            
            continue

        # at least in range, meeting tree
        if(matrix[candR][candC]==2):
            continue

        # valid next
        FrontEnd.append((candR,candC,d))

    if(len(FrontEnd)==0):
        return curR,curC
    else:
        nextR,nextC,d = FrontEnd.popleft()
        Migrant_Dir[num]=d
        return nextR,nextC

import string
def showmigrants(Migrant_COORD,matrix):
    tmp_matrix=[]
    for row in matrix:
        tmp_matrix.append(row[:])

    for num, cur in Migrant_COORD.items():
        tmp_matrix[cur[0]][cur[1]]=string.ascii_lowercase[num-1]
    print(Migrant_COORD)
    print(COORD_Migrant)
    print(*tmp_matrix,sep='\n')

if __name__=="__main__":
    T = int (sys.stdin.readline().strip())
    
    results=[]
    for testnum in range(1,T+1):
        N,K = map(int, sys.stdin.readline().split())

        matrix=[]
        COORD_Migrant = {}
        for _ in range(N):
            row=list(map(int, sys.stdin.readline().split()))
            matrix.append(row)
        # print(*matrix,sep='\n')

        Migrant_COORD = {}
        Migrant_Dir = {}

        COORD_Migrant = {}
        for k in range(1,K+1):
            r,c,d = map(int, sys.stdin.readline().split())
            Migrant_COORD[k]=(r,c)
            Migrant_Dir[k]=d

            if( (r,c) not in COORD_Migrant.keys()):
                COORD_Migrant[(r,c)]=list()
            COORD_Migrant[(r,c)].append(k)

        # print(Migrant_COORD)
        # print(Migrant_Dir)
        # print(COORD_Migrant)

        time=0
        token=True
        while(token):
            #per sec, A.L.L bird move based on condition
            for num,cur in Migrant_COORD.items():
                # print('--------cur time~before next', time, time+1)
                d=Migrant_Dir[num]
                # print('num, cur, d/', num,cur,d)
                nextR,nextC = move(num,cur,d)
                # print('next place ',nextR,nextC)
                # print()
                if((nextR,nextC)==cur): pass
                else:
                    # showmigrants(Migrant_COORD,matrix)

                    # slicing the parts; left or unit of gone
                    cand=COORD_Migrant[cur]
                    # print('cand at current ', cand)
                    std=cand.index(num)
                    # print('std index',std)
                    if(std==0): left=list()
                    else:  left=cand[:std]
                    unit=cand[std:]
                    # print('unit',unit)
                    # migrant 기준 갱신, 현재 넘버 뒤쪽으로만 이동
                    for num in unit:
                        Migrant_COORD[num]=(nextR,nextC)
                    # print('renew the migrant',Migrant_COORD)

                    # 좌표 기준 갱신, 단 next 칸의 빛이 없으면 아래, 있으면 위
                    if( (nextR,nextC) not in COORD_Migrant.keys()):
                        COORD_Migrant[(nextR,nextC)]=list()

                    # print('light or not', matrix[nextR][nextC])
                    if(matrix[nextR][nextC]==0): COORD_Migrant[(nextR,nextC)]=unit+COORD_Migrant[(nextR,nextC)]
                    elif(matrix[nextR][nextC]==1): COORD_Migrant[(nextR,nextC)]=COORD_Migrant[(nextR,nextC)]+unit
                    COORD_Migrant[cur]=left
                    if(len(COORD_Migrant[cur])==0): del COORD_Migrant[cur]
                    # print('renew the coord',COORD_Migrant)
                    # print()
                    # showmigrants(Migrant_COORD,matrix)

                    # 좌표 이동 후에, 즉 철새가 겹칠 수 있는 상황, 그 중 4마리 이상 겹치면 print and break
                    if(len(COORD_Migrant[(nextR,nextC)])>=4):
                        results.append((testnum,time+1))
                        token=False
                        break

            time+=1
            if(time==1000):
                results.append((testnum,-1))
                break

            # print()
    
    for result in results:
        print('#'+str(result[0]),result[1])