from collections import deque

def bfs(graph,v,visited):
    q=deque()
    q.append(v)
    visited[v]=1
    
    while(q):
        curV = q.popleft()
        
        for adj in graph[curV]:
            if(visited[adj] != 0): continue
            else:
                visited[adj]=1
                q.append(adj)

def solution(n, computers):
    answer = 0
    
    graph=[[] for _ in range(n)]
    visited=[0 for _ in range(n)]
    
    for v,infos in enumerate(computers):
        for adj,info in enumerate(infos):
            if(v==adj): continue
            else:
                if(info==1 and adj not in graph[v]):
                    graph[v].append(adj)
                    graph[adj].append(v)
                    
    print(graph)
    
    for v in range(n):
        if(visited[v]==0):
            bfs(graph,v,visited)
            answer+=1
        else: continue
    print(answer)
    return answer