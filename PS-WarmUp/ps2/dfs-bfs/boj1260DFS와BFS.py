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

def dfs(graph,visited,v):
    visited[v]=1
    print(v, end=' ')
        

    for adj in sorted(graph[v]):
        if(visited[adj]==0):
            dfs(graph,visited,adj)

def bfs(graph,visited,s):
    visited[s]=1
    q=deque()
    q.append(s)

    while q:
        now = q.popleft()
        print(now, end=' ')

        for adj in graph[now]:
            if(visited[adj]==0):
                visited[adj]=1
                q.append(adj)


if __name__=="__main__":
    n,m,s=map(int,input().split())

    graph=defaultdict(list)

    for _ in range(m):
        v1,v2=map(int,input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    # 정점번호가 작은것부터 방문하도록 미리 정렬 
    
    for key,val in graph.items():
        val.sort()
        # print(key,val)
    
    # 정점번호 1부터 시작
    visited=[0]+[0 for _ in range(n)]
    dfs(graph,visited,s)
    print()
    visited=[0]+[0 for _ in range(n)]
    bfs(graph,visited,s)