import sys
from collections import deque

'''
1. 그냥 테두리 값들 추출해서 1번 rotate 후 재배치
2. push robot으로 1개씩 이동하면서 변환

1번이 N,M이 고정이라 구현이 더 쉬울것같은데, 일단 범용성차원에서 2로 결정
추가로 방문 및 로직의 편리성을 위해서 시작 위치를 좌상 에서 1칸 오른쪽으로
=> wrong, 일단 구현쉬운걸로 하자.

'''

# def pushrobot(idx_r, idx_c):
#     global N,M,matrix

#     while(1):
#         #현재 블록 보존, 다음을 위해
#         tmp_fornextblock=matrix[idx_r][idx_c]

#         #

def getedge():
    global N,M,matrix
    edges=[]
    # 시작점은 그냥 맨 좌상 좌표로 고정
    # !! below r and c imply index of computer 0~
    cur_r=0;cur_c=0

    cand_r=-1;cand_c=-1

    # magnitue : mag
    # direction : East, south, west, north 
    mag=1
    dr=[0,mag,0,-mag]
    dc=[mag,0,-mag,0]

    d=0
    # kinds_vector=len(dr)
    # for d in range(kinds_vector):
    # 현재 위치에서 4방면 체크라면 위와같은 것이겠지만, 현재는 1방향이고, 
    # 조건에 따라서 d 전환 체제

    while(1):
        # current
        # print(cur_r, cur_c)
        edges.append(matrix[cur_r][cur_c])
        # print(edges)

        cand_r=cur_r+dr[d]
        cand_c=cur_c+dc[d]

        # 다음이 맵 밖이면 방향전환 후 이동
        # print('dir ',d)
        if(cand_r<0 or cand_r>(N-1) or cand_c<0 or cand_c>(M-1)):
            d= (d+1)%4
            cand_r=cur_r+dr[d]
            cand_c=cur_c+dc[d]
        
        # 다시 처음으로 돌아오면 끝
        if(cand_r==0 and cand_c==0):
            break

        cur_r=cand_r
        cur_c=cand_c

    # print(edges)
    return edges

def setedge(deque_edge):
    global N,M,matrix

    # !! below r and c imply index of computer 0~
    cur_r=0;cur_c=0

    cand_r=-1;cand_c=-1

    # magnitue : mag
    # direction : East, south, west, north 
    mag=1
    dr=[0,mag,0,-mag]
    dc=[mag,0,-mag,0]

    d=0
    while(1):
        # current
        # print('set ',cur_r, cur_c)
        matrix[cur_r][cur_c]=deque_edge.popleft()

        cand_r=cur_r+dr[d]
        cand_c=cur_c+dc[d]

        # 다음이 맵 밖이면 방향전환 후 이동
        if(cand_r<0 or cand_r>(N-1) or cand_c<0 or cand_c>(M-1)):
            d= (d+1)%4
            cand_r=cur_r+dr[d]
            cand_c=cur_c+dc[d]
        
        # 다시 처음으로 돌아오면 끝
        if(cand_r==0 and cand_c==0):
            break

        cur_r=cand_r
        cur_c=cand_c


def pushedge():
    global N,M,matrix

    #get edges
    edges_matrix=[]
    edges_matrix=getedge()
    # print(edges_matrix)
    
    #rotate
    deque_edge=deque(edges_matrix)
    deque_edge.rotate(1)
    # print(deque_edge)

    #set matrix
    setedge(deque_edge)

    # print(*matrix,sep='\n')
    for row in matrix:
        print(' '.join(map(str,row)))


if __name__=="__main__":
    global N,M
    N,M = map(int, sys.stdin.readline().split())

    global matrix
    matrix=[]
    for _ in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    pushedge()


