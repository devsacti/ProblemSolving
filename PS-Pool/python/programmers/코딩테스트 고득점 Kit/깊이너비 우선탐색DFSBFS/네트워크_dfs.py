# ps1. comprehension
# 인접행렬 -> 인접리스트
# dfs와 그 기능이 보장된다면, 우리는 visted가 0인 노드를 통해서 네트워크 수를 셀수있다.
# 왜냐하면 처음 한번도 방문하지 못한 노드에 대해서 dfs를 하면 그와 연결된 노드들 모두 visited가 1로 될것이고,
# 모든 노드들에 dfs를 돌리면 네트워크 단위로 visited가 1이 되기 때문에 
# 모든 노드에 대한 dfs가 전제될 때 dfs 직전 visited가 0인 노드 수를 세면 네트워크 수를 셀수있다.

# ps2. applying algorithms
# dfs

# ps3. impl
#
from collections import defaultdict

def dfs(graph, visited, v):
    visited[v]=1

    for adj in graph[v]:
        if(visited[adj]==0):
            dfs(graph,visited,adj)

def solution(n, computers):
    global answer
    answer = 0
    # graph :: tree
    graph=defaultdict(list)
    visited={key:0 for key in range(1,n+1)}
    
    for r in range(1,n+1):
        for c in range(1,n+1):
            if(r==c):
                continue
            else:
                if(computers[r-1][c-1]==1):
                    graph[r].append(c)

    
    # for key,val in graph.items():
    #     print(key,val)
    
    for v in range(1,n+1):
        if visited[v]==0:
            answer+=1
        dfs(graph,visited,v)
    
    
    return answer