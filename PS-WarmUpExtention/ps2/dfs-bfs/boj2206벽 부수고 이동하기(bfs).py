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

module 2 : based on coord of walls, assume certain coord of wall is delete, then get shortest
!! 시간 초과 발생, 우선 이미 방문한 인접노드 방문횟수를 줄이고, 인접노드 평가를 간소화하고, 2d 매트릭스 선언횟수를 줄였으나, 역부족
!! => bfs 호출횟수를 줄인다.

module 2.1. : by bfs check the shortest, or invalid
!! 최단경로의 정의는 지나간 칸 수인데, 시작칸도 포함하므로 +1

ps2.2. integrations

ps3. Impl
'''
from collections import deque

# bfs
def bfs(graph, visited, matrix_cost):
    global start,end
    r_start, c_start = start
    cost = 0 
    visited[r_start][c_start]=1
    q=deque()
    q.append((r_start,c_start,cost))

    # direction vector ; updown, leftright
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    while q:
        r_now,c_now, cost_now = q.popleft()

        matrix_cost[r_now][c_now]=cost_now

        # get valid adjs
        adjs=[]

        for dir in range(len(dr)):
            r_adj=r_now+dr[dir]
            c_adj=c_now+dc[dir]

            if(r_adj>(n-1) or r_adj<0 or c_adj > (m-1) or c_adj < 0):
                continue

            if(graph[r_adj][c_adj]==1):
                continue

            if(visited[r_adj][c_adj]==1):
                continue

            adjs.append((r_adj,c_adj))

        for adj in adjs:
            r_adj,c_adj=adj
            if(visited[r_adj][c_adj]==0):
                visited[r_adj][c_adj]=1
                q.append((r_adj,c_adj,cost_now+1))

    # print(*matrix_cost,sep='\n')
    # print()
    r_end,c_end=end
    # print(matrix_cost[r_end][c_end])
    # if(matrix_cost[r_end][c_end]==19):
    #     print(*matrix_cost,sep='\n')
    return matrix_cost[r_end][c_end]

if __name__=="__main__":
    # module 1.
    global n,m
    n,m = map(int, input().split())
    # coord of start,end based on 0 indexing
    global start, end
    start=(n-1,0)
    end=(0,m-1)

    matrix_maze=[list(map(int,list(input().split()))) for _ in range(n)]
    matrix_cost=[[0]*m for _ in range(n)]
    # print(*matrix_maze,sep='\n')

    coord_walls=[]
    for r in range(n):
        for c in range(m):
            if(matrix_maze[r][c]==1):
                coord_walls.append((r,c))
    # print(coord_walls)

    # module 2.

    min_shortest=int(1e20)
    token_update=False
    for certain_coord in coord_walls:
        r,c=certain_coord
        # 시간초과 대응 => 해당 나무 삭제 후 추후 복구
        matrix_maze[r][c]=0

        # module 2.1.
        visited=[[0]*m for _ in range(n)]
        # reinit per deleting certain coord
        matrix_cost=[[0]*m for _ in range(n)] 
        
        cand_shortest=bfs(matrix_maze,visited,matrix_cost)

        if(cand_shortest != 0 and cand_shortest<min_shortest):
            min_shortest=cand_shortest
            token_update=True
        # 복구
        matrix_maze[r][c]=1

    if(not token_update):
        min_shortest=-1

    print(min_shortest)