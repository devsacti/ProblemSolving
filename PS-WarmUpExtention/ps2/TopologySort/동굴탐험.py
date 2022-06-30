'''
https://programmers.co.kr/learn/courses/30/lessons/67260

'''

# ps1. comprehension about problem
# 양방향, DAG가 아니므로 커스텀 필요, DAG를 만들어야하고, 기본 indegree에 추가 조건에 따른 값보정 필요

# ps2. Applying computer algorithms

# ps3. Impl
from collections import defaultdict
from collections import deque

# bfs for DAG and basic indegree
# graph, visitd is global
def bfs(s,n):
    visited[s]=True
    q=deque()
    q.append(s)
    
    while q:
        now = q.popleft()
        
        for adj in graph[now]:
            if visited[adj]:
                continue
            
            DAG[now].append(adj)
            indegree[adj]+=1
            
            visited[adj]=True
            q.append(adj)
    

# DAG, indegree is global
def topologysort(n):
    q=deque()
    answer=True
    progress_move=[]
    
    for i in range(n):
        if(indegree[i]==0):
            q.append(i)
    # print('start candiates', q)
    
    for i in range(n):
        if not q:
            answer=False
            break
        
        now = q.popleft()
        progress_move.append(now)
        
        for adj in DAG[now]:
            indegree[adj]-=1
            
            if indegree[adj] == 0:
                q.append(adj)
                
    # print('progress_move',progress_move)
    
    return answer

def solution(n, path, order):
    global graph, visited
    global DAG, indegree
    
    graph = defaultdict(list)
    visited = {k : False for k in range(n)}
    
    DAG = defaultdict(list)
    indegree = {k:0 for k in range(n)}
    
    for edge in path:
        v1,v2=edge
        
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    # for key, val in graph.items():
    #     print(key,val)
        
    # bfs, start is given 0
    # bfs for configuring DAG and basic indegree
    s=0
    bfs(s,n)
    
    # for key, val in DAG.items():
    #     print(key,val)

    # 문제 조건에 따른 추가 indegree 조정
    for condi in order:
        v1,v2 = condi
        
        # 현재 움직임에서 order에 따라 indegree가 추가됨은 물론 
        # 연관관계의 선수 노드 방문 시, 지난 길을 되돌아가는 로직은 생략가능하므로
        # 후속 노드는 인접하게 생각가능!
        DAG[v1].append(v2)
        indegree[v2]+=1
        
    # print(indegree)
        
    answer = topologysort(n)
    return answer