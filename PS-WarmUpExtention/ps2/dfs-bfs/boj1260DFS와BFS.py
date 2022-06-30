'''
reference : https://www.acmicpc.net/problem/1260

ps1. comprehension for problem
ps1.1. analysis

vertex numbering ; 1 ~ N
양방향이고, 갈림길에서는 노드 넘버가 작은 순으로 방문

ps1.2. drawing pattern, exception

dfs,bfs

ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing

module 1 ; recursive

ps2.2. integrations
ps2.3. humble approach

ps3. Impl
'''
from collections import defaultdict
from collections import deque

def dfs(graph,visited,now):
    visited[now]=1
    print(now, end=' ')

    # 오름차순으로 정점 방문
    adjs = sorted(graph[now])

    for adj in adjs:
        if(visited[adj]==0):
            dfs(graph,visited,adj)

def bfs(graph,visited,s):
    visited[s]=1
    q=deque()
    q.append(s)

    while q:
        now = q.popleft()
        print(now,end=' ')

        # 오름차순으로 인접 노드 방문
        adjs=sorted(graph[now])

        for adj in adjs:
            if(visited[adj]==0):
                visited[adj]=1
                q.append(adj)

if __name__=="__main__":
    n,m,v = map(int, input().split())

    vertexes=[i for i in range(1,n+1)]

    graph=defaultdict(list)
    # 1 based indexing
    visited=[0]+[0 for _ in range(n)]


    for _ in range(m):
        v1,v2 = map(int,input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    keys=list(graph)

    # for key in keys:
    #     print(key, graph[key])

    dfs(graph,visited,v)

    # 1 based indexing ;reinit
    print()
    visited=[0]+[0 for _ in range(n)]
    bfs(graph,visited,v)