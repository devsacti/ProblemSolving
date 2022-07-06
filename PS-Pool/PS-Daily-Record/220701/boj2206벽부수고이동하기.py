# https://www.acmicpc.net/problem/2206

# ps1.

## (1,1)부터 시작, 최단 경로, 
## 시작하는 칸과 마지막 칸도 포함
## 벽 1개 부수기 가능


# ps2.

# ps3.
from collections import defaultdict
from collections import deque

# bfs move from s
def move_s(matrix, visited, s, dist):
    init_r, init_c = s
    init_cost = 1
    visited[init_r][init_c]=1
    q=deque()
    q.append((init_r,init_c,init_cost))
    
    #
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    while q:
        now_r,now_c,now_cost = q.popleft()
        

        if(dist[now_r][now_c]==0):
            dist[now_r][now_c]=now_cost
        # print(now_r,now_c)
        # print(*dist,sep='\n')
        # print()

        adjs=[]
        for i in range(4):
            cand_r = now_r + dr[i]
            cand_c = now_c + dc[i]

            if(cand_r<0 or cand_r>(n-1) or cand_c<0 or cand_c>(m-1)):
                continue

            if(matrix[cand_r][cand_c]==1):
                if(dist[cand_r][cand_c]==0):
                    dist[cand_r][cand_c]=now_cost+1
                else:
                    dist[cand_r][cand_c]=min(dist[cand_r][cand_c],now_cost+1)
                continue

            if(visited[cand_r][cand_c]==1):
                continue

            adjs.append((cand_r,cand_c))
        # print('adjs',adjs)
        # print()

        for adj in adjs:
            next_r,next_c=adj
            next_cost=now_cost+1

            if(visited[next_r][next_c]==0):
                visited[next_r][next_c]=1
                q.append((next_r,next_c,next_cost))

if __name__=="__main__":
    global n,m
    n,m=map(int,input().split())
    
    matrix=[]

    for _ in range(n):
        row=list(map(int,input()))
        matrix.append(row)

    # print(*matrix,sep='\n')

    # coordinates of walls
    walls=[]
    for r in range(n):
        for c in range(m):
            if(matrix[r][c]==1):
                walls.append((r,c))
    
    s=(0,0)
    visited=[[0]*m for _ in range(n)]
    dist=[[0]*m for _ in range(n)]
    move_s(matrix, visited, s, dist)
    # print(*dist,sep='\n')
    # print()

    s=(n-1,m-1)
    visited=[[0]*m for _ in range(n)]
    dist2=[[0]*m for _ in range(n)]
    move_s(matrix, visited, s, dist2)
    # print(*dist2,sep='\n')
    

    answer=int(1e10)
    if(dist[n-1][m-1]==0):
        pass
    else:
        answer=dist[n-1][m-1]

    for wall in walls:
        wall_r, wall_c = wall

        if(dist[wall_r][wall_c] !=0 and dist2[wall_r][wall_c] !=0):
            cand_answer=dist[wall_r][wall_c]+dist2[wall_r][wall_c]-1
            answer=min(cand_answer,answer)

    if(answer==int(1e10)):
        print(-1)
    else:
        print(answer)