# 2 차원 배열 위에서 아래와같은 번호순으의 벡터 구현하기

# [1,2]
# [4,3]

# [1,2,9]
# [4,3,8]
# [5,6,7]

# [1,2,9,10]
# [4,3,8,11]
# [5,6,7,12]
# [16,15,14,13]

# ps1.

# ps1.2 drawing pattern
# 부담스러운 0,0은 제외하고 이해하면 단순 벡터의 움직임
# 
#        n=2    n=3   n=4
# 시작점 (0,1)        (0,3)       (0,5)
#              (2,0)        (4,0)       

from collections import deque

def bfs_robot(matrix, s, visited):
    r_s,c_s=s
    visited[r_s][c_s]=1
    q=deque()
    q.append(s)

    #
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    # direction ; 시계방향으로 시작
    clockwise=1

    while q:
        r_now, c_now = q.popleft()

        adjs=[]

def vector_rook(matrix,start):
    global flag
    r_start,c_start=start
    
    # row of start is 0 and column of start is not 0 case ; down and left direction
    # row of start is not 0 and column of start is 0 case ; right and up direction
    if(r_start==0):
        dr=[1,0]
        dc=[0,-1]
    else:
        dr=[0,-1]
        dc=[1,0]

    # row of start is 0 and column of start is not 0 case ; magnitude is val of column
    # row of start is not 0 and column of start is 0 case ; otherwise
    if(r_start==0):
        magnitude=c_start
    else:
        magnitude=r_start

    # flag at start point
    matrix[r_start][c_start]=flag
    flag+=1
    # print('start point',start)
    # vector consists of magnitude and direction
    for i in range(len(dr)):
        for m in range(1,magnitude+1):
            r_move=r_start+dr[i]*m
            c_move=c_start+dc[i]*m

            # print('next move point',r_move,c_move)
            matrix[r_move][c_move]=flag
            flag+=1
            # print(*matrix,sep='\n')
            # print()

        r_start=r_move
        c_start=c_move

if __name__=="__main__":
    n=int(input())

    matrix=[[0]*n for _ in range(n)]
    
    global flag
    flag=1
    matrix[0][0]=flag
    flag+=1

    # print(*matrix,sep='\n')

    starts=[]
    for s_val in range(1,n):
        if(s_val%2!=0):
            element=[0,s_val]
        else:
            element=[s_val,0]
        starts.append(element)

    # print(starts)

    for start in starts:
        vector_rook(matrix,start)

    print(*matrix,sep='\n')

    print()
    pre_matrix=list(zip(*matrix))
    transposed_matrix=[list(row) for row in pre_matrix]

    print(*transposed_matrix,sep='\n')
