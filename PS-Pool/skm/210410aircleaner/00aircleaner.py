# 공기청정기
# 일자 오전 11:55 2021-04-20
# 개요
# 공기 오염의 확산을 시뮬레이션하고, 공기청정기의 작동을 시뮬레이션 한다.
# main consists of 'spread', 'pushrobot' as a MAJOR MODULE
## spread has 'spreadDelta' as a SUB MODULE

# tcp 1 시간 줄이고자 set 함수 안쓰고 방향벡터 생성

import sys
from collections import deque

# global variables
global R,C,S,K
global matrix, updatedMatrix
global upR, downR
global dir_vectors

# SUB MODULE OF spread
def spreadDelta( stdR, stdC, delta):
    global R,C,matrix,updatedMatrix
    global dir_vectors
    global K

    # valid delta 에 대해서 방향벡터를 통해 인접노드들 판단
    for vector in dir_vectors:
        cand_r=stdR+vector[0]
        cand_c=stdC+vector[1]

        if( cand_r<0 or cand_r>R-1 or cand_c<0 or cand_c>C-1):
            continue

        # exclude the place of aircleaner, it should not be effected at 'spreadDelta'
        if(matrix[cand_r][cand_c]==-1):
            continue
        
        # STEP 선별된 인접노드들 에 delth를 빼서 뿌리고 반영
        adjR, adjC = cand_r, cand_c
        # deltha will be stacked so +=
        updatedMatrix[stdR][stdC]+= -delta
        updatedMatrix[adjR][adjC]+= delta

# MAJOR MODULE
def spread():
    global R,C,K
    global matrix, updatedMatrix

    updatedMatrix=[[0]*C for _ in range(R)]

    # 방문 좌표를 기준으로 삼아
    # spreadDelth를 호출해서 범위 내 인접노드에 오염를 분배한다.
    for stdR in range(R):
        for stdC in range(C):
            # stdR,stdC ; INDEX OF COMPUTER
            delta = matrix[stdR][stdC] // (2*(K**2)+2*K+1)
            if(matrix[stdR][stdC] == -1 or delta == 0 ):
                # aircleaner or 0 has no contamination Value to spread
                pass
            else:
                # 기준 노드를 중심으로 주변에 분배되야할 delta값 주고, 과정중 기준노드에 차감정도 반영
                spreadDelta(stdR,stdC, delta)
            # at result, update the base
            updatedMatrix[stdR][stdC]+=matrix[stdR][stdC]

    # print(*updatedMatrix,sep='\n')
    # print('--')
        
    for idx, row in enumerate(updatedMatrix):
        matrix[idx]=row

    # print('matrix')
    # print(*matrix,sep='\n')
    # print('--')

# MAJOR MODULE  ; push robot of Aircleaner
def pushrobot(startR, startC):
    global R,C,matrix
    global upR, downR
    # 구현 간소화를 위해 현재 지점을 공기청정기 앞부터 시작
    curR,curC = startR, startC-1
    # init next
    nextR, nextC = -1, -1
    
    # q is for waiting line of values for set, 0 means first clean air
    q=deque()
    q.append( matrix[curR][curC] )
    matrix[curR][curC]=0

    # direction vectors per updown; m is magnitude
    m=1
    if(startR == upR):
        dr=[0,-m,0,m]
        dc=[-m,0,m,0]
    else:
        dr=[0,m,0,-m]
        dc=[-m,0,m,0]
    kinds_dir=len(dr)
    d=0

    # not(startR == nextR and startC == nextC) is same with below
    while( curR != startR or curC != startC ):
        # next 탐색
        candR=curR+dr[d]
        candC=curC+dc[d]
        # print(candR,candC,curR,curC)
        if(startR == upR):
            if(candR<0 or candR>upR or candC<0 or candC>C-1):
                d+=1
                candR=curR+dr[d]
                candC=curC+dc[d]
            
        elif(startR == downR):
            if(candR<downR or candR>R-1 or candC<0 or candC>C-1):
                d+=1
                candR=curR+dr[d]
                candC=curC+dc[d]
        # print('#',candR,candC,curR,curC)

        # possible next by if judgement
        nextR, nextC = candR, candC
        q.append(matrix[nextR][nextC])

        #go to next spot
        curR, curC = nextR, nextC
        # set the value except when current is place of aiclreaner
        if(matrix[curR][curC]!=-1):matrix[curR][curC] = q.popleft()
        else: pass

if __name__=="__main__":
    T = int(sys.stdin.readline().strip())

    total_pollution=[]
    for t in range(T):
        R,C,S,K = map(int, sys.stdin.readline().split())
        # print(R,C,S,K)

        matrix = []
        for _ in range(R):
            row = list(map(int, sys.stdin.readline().split()))
            matrix.append(row)
        updatedMatrix=[]

        # find aircleaner's row idx; upR or downR of Aircleaner ; INDEX OF COMPUTER
        # -1 in matrix means place of aircleaner
        # it is placed at right side
        for idx, row in enumerate(matrix):
            if(row[-1] == -1):
                upR=idx
                downR=idx+1
                break

        # simulation per Second
        # 1. spread
        # 2. next airclean robot

        #dir vector for spread
        dir_vectors=[]
        for subk in range(1,K+1):
            for dr in range(0,subk+1):
                arrange_li=[]
                # (subk-dr) means column
                arrange_li.append( (+dr,+(subk-dr)) )

                # 절편인 경우들
                if( dr == 0):
                    arrange_li.append( (+dr,-(subk-dr)) )
                if( (subk-dr) == 0 ):
                    arrange_li.append( (-dr, (subk-dr)) )

                # 절편이 아닌 경우
                if( dr != 0 and  (subk-dr) !=0):
                    arrange_li.append( (+dr,-(subk-dr)) )
                    arrange_li.append( (-dr, (subk-dr)) )
                    arrange_li.append( (-dr,-(subk-dr)) )

                dir_vectors.extend(arrange_li)
        # print(dir_vectors)

        for _ in range(S):
            spread()
            pushrobot( upR, C-1 )
            # print(*matrix,sep='\n')
            # print('==')
            pushrobot( downR, C-1 )
            # print(*matrix,sep='\n')

        tmp_contamination=0
        for row in matrix:
            tmp_contamination+=sum(row)
        # +2 cuz to aircleaner -1 and -1
        total_pollution.append(tmp_contamination+2)
        # print(total_pollution)
        # 

    for t in range(T):
        print('#'+str(t+1),total_pollution[t])