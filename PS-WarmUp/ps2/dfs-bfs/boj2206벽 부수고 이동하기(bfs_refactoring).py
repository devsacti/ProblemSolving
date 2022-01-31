'''
reference : https://www.acmicpc.net/problem/2206

ps1. comprehension of problem
ps1.1. analysis

from (1,1) to (N,M) 최단거리; 1 base indexing 
1 하나 삭제 가능
상하좌우로만 이동

ps1.2. drawing pattern, exception

bruteforce 방식으로 벽마다 사라졌을때의 최단거리를 구한다.

ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing computer algorithms

module 1 : make 2d matrix and check coord of walls

module 2 : respectively per point of start, end, execute bfs, then get matrix cost of start, end

then assume certain wall of walls is deleted,but not really deleting wall_making 1 as 0_,then drawing shortest

fomular ; shortest = matrix_cost_s[r_assumed][c_assume] + 1 + matrix_cost_e[r_assumed][c_assume]
=> 해당 벽이 없어졌다고 가정 후, 이 벽의 좌표 4방위에 연결할 길이 있나 봐야한다.
=> 근데 4방위로 난 길이 각각 s에서 시작된건지, e에서 시작된건지 복잡
=> 해당 벽까지의 거리를 업데이트하자, 방문처리는 안하더라도

!! 최단경로의 정의는 지나간 칸 수인데, 시작칸과 끝칸도 포함하여 

ps2.2. integrations

ps3. Impl
'''
from collections import deque

# bfs
def bfs(graph, visited, start,matrix_cost):
    r_start, c_start = start
    # 시작칸도 체크
    cost = 1
    visited[r_start][c_start]=1
    q=deque()
    q.append((r_start,c_start,cost))

    # direction vector ; updown, leftright
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    while q:
        r_now,c_now, cost_now = q.popleft()

        if(matrix_cost[r_now][c_now]==0):
            matrix_cost[r_now][c_now]=cost_now
        else:
            matrix_cost[r_now][c_now]=min(cost_now,matrix_cost[r_now][c_now])

        # get valid adjs
        for dir in range(len(dr)):
            r_adj=r_now+dr[dir]
            c_adj=c_now+dc[dir]

            if(r_adj>(n-1) or r_adj<0 or c_adj > (m-1) or c_adj < 0):
                continue

            if(graph[r_adj][c_adj]==1):
                if(matrix_cost[r_adj][c_adj]==0):
                    matrix_cost[r_adj][c_adj]=(cost_now+1)
                else:
                    matrix_cost[r_adj][c_adj]=min(cost_now+1,matrix_cost[r_adj][c_adj])
                continue

            if(visited[r_adj][c_adj]==1):
                continue

            visited[r_adj][c_adj]=1
            q.append((r_adj,c_adj,cost_now+1))

    return matrix_cost

if __name__=="__main__":
    # module 1.
    global n,m
    n,m = map(int, input().split())
    # coord of start,end based on 0 indexing
    start=(0,0)
    end=(n-1,m-1)

    matrix_maze=[list(map(int,list(input()))) for _ in range(n)]
    # print(*matrix_maze,sep='\n')

    coord_walls=[]
    for r in range(n):
        for c in range(m):
            if(matrix_maze[r][c]==1):
                coord_walls.append((r,c))
    # print(coord_walls)

    # module 2.
    matrix_cost_s=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    matrix_cost_s=bfs(matrix_maze,visited,start,matrix_cost_s)
    # print(*matrix_cost_s,sep='\n')
    # print()

    matrix_cost_e=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    matrix_cost_e=bfs(matrix_maze,visited,end,matrix_cost_e)
    # print(*matrix_cost_e,sep='\n')
    
    # 벽 제거 없이 도달가능하다면 start든 end든 costmatrix에 업데이트 되므로 1개만 체크
    min_shortest=int(1e20)

    token_min_update=False
    if(matrix_cost_s[end[0]][end[1]]!=0):
        min_shortest=matrix_cost_s[end[0]][end[1]]
        token_min_update=True
    
    for certain_coord in coord_walls:
        r,c=certain_coord
        # print(certain_coord,end=' ')
        # start와 end에서 모두 접근 가능한 벽에 한정하여 계산
        if(matrix_cost_s[r][c] !=0 and matrix_cost_e[r][c] !=0):
            # 중복칸 제거
            tmp_shortest=matrix_cost_s[r][c]+matrix_cost_e[r][c]-1
            # print(tmp_shortest, min_shortest)
            if(tmp_shortest<min_shortest):
                min_shortest=tmp_shortest
                token_min_update=True

    if(not token_min_update):
        min_shortest=-1

    print(min_shortest)