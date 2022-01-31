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

module 2 : respectively per point of start, end, execute dfs, then get matrix cost of start, end

then assume certain wall of walls is deleted,but not really deleting wall_like making 1 as 0_,then drawing shortest

by plus dist from start and dist from end with reducing error of measurement

!! 
dfs의 방문 진행이 중간에 벽으로 인해 최적이 아니라, 돌아가게 되고, 또한 그렇게 생긴 오차를 다른 경로 갱신과정에서 수정불가한 경우가 발생하였다.
(input)
6 4
0100
1110
1000
0000
0111
0000
(output)
matrix of cost
[0, 16, 15, 14]
[0, 9, 10, 11]
[7, 8, 9, 10]
[6, 7, 8, 9]
[5, 4, 3, 2]
[4, 3, 2, 1]
* boj2206 input-output record 참고
위에서 코스트가 11로 갱신된곳은 dfs 접근 경로 상 13이었지만 다른 dfs 경로에서 최소값이 갱신되어 11로 수정되었으나,
첫번째 row의 경우, dfs 경로가 유일하고, 이 dfs 경로가 최적이 아니라서 큰 오차가 발생하였다.

이를 오차를 잡기 위해 dfs 후에
bfs를 별도로 돌려서 맞닿은 노드끼리는 코스트가 1차이나게 수정할 수 있으나,
이는 결국 bfs이다.

어떻게든 dfs로 구현은 되겠지만, 거리 관련해서는 bfs에 비해 ps1.2.이 ps2.1.로 코드화되는 과정이 덜 매끄럽다.
그러므로 이는 bfs를 채택하는 것으로 마무리

ps2.2. integrations

ps3. Impl
'''
from collections import deque

# dfs
def dfs(graph,visited,now,matrix_cost,cost_now):
    global n,m
    r_now,c_now=now
    print(now, cost_now)
    print(*matrix_cost,sep='\n')
    print()
    visited[r_now][c_now]=1

    if(matrix_cost[r_now][c_now]==0):
        matrix_cost[r_now][c_now]=cost_now
    else:
        matrix_cost[r_now][c_now]=min(cost_now,matrix_cost[r_now][c_now])

    # direction vector ; updown, leftright
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    # get valid adjs
    adjs=[]
    for idx_dir in range(len(dr)):
        r_adj=r_now+dr[idx_dir]
        c_adj=c_now+dc[idx_dir]

        if(r_adj>(n-1) or r_adj<0 or c_adj>(m-1) or c_adj<0):
            continue

        # 애당초 방문안한 노드만 처리하는 부분이지만, 문제 접근 방식상,
        # 벽이더라도, 혹은 이미 방문한 노드더라도 최소값을 갱신해야한다.
        # 그 다음 다음 노드로 진행
        if(graph[r_adj][c_adj]==1 or visited[r_adj][c_adj]==1):
            if(matrix_cost[r_adj][c_adj]==0):
                matrix_cost[r_adj][c_adj]=(cost_now+1)
            else:
                matrix_cost[r_adj][c_adj]=min((cost_now+1),matrix_cost[r_adj][c_adj])
            continue

        adjs.append((r_adj,c_adj))

    for adj in adjs:
        dfs(graph,visited,adj,matrix_cost, cost_now+1)

if __name__=="__main__":
    # module 1.
    global n,m
    n,m = map(int, input().split())
    # coord of start,end based on 0 indexing
    global start, end
    start=(0,0)
    end=(n-1,m-1)

    matrix_maze=[list(map(int,list(input()))) for _ in range(n)]
    matrix_cost=[[0]*m for _ in range(n)]
    # print(*matrix_maze,sep='\n')

    coord_walls=[]
    for r in range(n):
        for c in range(m):
            if(matrix_maze[r][c]==1):
                coord_walls.append((r,c))
    # print(coord_walls)

    # module 2.
    # start side
    matrix_cost_s=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    cost_now=1
    dfs(matrix_maze,visited,start,matrix_cost_s,cost_now)
    print(*matrix_cost_s,sep='\n')
    print()
    # end side
    matrix_cost_e=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    cost_now=1
    dfs(matrix_maze,visited,end,matrix_cost_e,cost_now)
    print(*matrix_cost_e,sep='\n')

    # print(min_shortest)