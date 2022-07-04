# https://www.acmicpc.net/problem/2178

# ps1.
# 최소 칸 수

# ps2.

# ps3.
from collections import deque

def bfs(matrix, s, visited,dist):
    init_r, init_c = s
    init_cost=1
    visited[init_r][init_c]=1
    q=deque()
    q.append((init_r,init_c,init_cost))

    # 상하좌우
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    while q:
        now_r, now_c, now_cost = q.popleft()
        dist[now_r][now_c]=now_cost

        adjs=[]
        for i in range(4):
            cand_r=now_r+dr[i]
            cand_c=now_c+dc[i]

            if(cand_r<0 or cand_r>(n-1) or cand_c<0 or cand_c>(m-1)):
                continue

            if(matrix[cand_r][cand_c]==0):
                continue

            adjs.append((cand_r,cand_c))
        

        for adj in adjs:
            next_r, next_c = adj
            next_cost = now_cost + 1
            if(visited[next_r][next_c]==0):
                visited[next_r][next_c]=1
                q.append((next_r, next_c,next_cost))

    print(dist[n-1][m-1])

if __name__=="__main__":
    global n,m
    n,m = map(int,input().split())

    matrix=[]
    for _ in range(n):
        row=list(map(int,input()))
        matrix.append(row)

    visited=[[0]*m for _ in range(n)]
    dist=[[int(1e10)]*m for _ in range(n)]

    s=(0,0)
    bfs(matrix, s, visited,dist)