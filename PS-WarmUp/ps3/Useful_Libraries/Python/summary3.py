# graph
from collections import defaultdict
# !! vecter graph or tree 도 기억할 것!

# dfs bfs
from collections import deque
# dijstra : bfs + priority queue(heap)
from heapq import *
import heapq

## heapq는 오름차순으로 주어진 값을 정렬하는 최소힙
heap=[1,2,3,4,5]
heapq.heapify(heap)
heapify(heap)
# or
pq=[]
for item in heap:
    heappush(pq,item)
## 별도의 우선순위 산출을 통해, 가령 -, (0,origin9),(1,origin3) 등으로 재정렬 가능
for item in heap:
    heappush(pq,(-item,item))

## 특성상 pq[0]은 최소값이다. 현재 트리의 root
## 하지만, 방금 뽑아낸 값과 그 다음 트리의 root를 비교 시에 적합
## 다중정렬에는 부적합

def dfs(graph,v,visited,*arg):
    visited[v]=1

    for adj in graph[v]:
        if(visited[adj]==0):
            dfs(graph,v,visited,*arg)
        else:
            pass

def bfs(graph,s,visited,*arg):
    # this visited means 'will be visited'
    visited[s]=1
    q=deque()
    q.append(s)
    
    while(q):
        now=q.popleft()

        for adj in graph[now]:
            if(visited[adj]==0):
                visited[adj]=1
                q.append(adj)
            else:
                pass

def dijkstra(graph,s,shortest,*arg):
    # visited 처럼, 해석하면 안됨, 이 문제는 visited는 논외이고,
    # 최단거리를 도출하기 위한 적절한 초기화과정으로 이해해야함, 아래 2 스텝을 이해하기 위해
    ## 시작점 관련해서는 출입문이 2개이고 0과 20이라고 하자
    ## 그리고 초기화는 20으로 되있어서 부득이 내가 0으로 기입한 상황
    shortest[s]=0
    pq=[]
    heappush(pq,(0,s))

    while(pq):
        # 다음 노드까지의 '여러가지 접근 경로가 존재하는 상황'에서, 최단거리를 찾는과정
        # 1. 현재 노드까지의 거리가 최단거리로서 가치가 있는가? => 최소한 지금까지 갱신된 최단거리보다는 작아야한다. 그렇지않다면 버린다.(continue)
        # 2. 그렇다면, 현재 위치에서 다음 노드를 접근할때의 거리의 합은 인접노드의 최단거리를 산출하는 '후보'로서 자격이 있다.
        
        # part of 1
        # candidate of shortest when we visit now node
        cand_shortest_now, now = heapq.heappop(pq)
              
        if(cand_shortest_now>shortest[now]): 
            continue
        else:
            # part of 2
            # 현재 노드까지의 최단거리로서 가치 있는 후보라면, 이 후보를 바탕으로 다음 인접노드의 최단거리의 '후보'를 구할 자격이 있다.
            for adj in graph[now]:
                interval,idx_adj=adj
                cand_shortest_adj=cand_shortest_now+interval

                if(cand_shortest_adj<shortest[idx_adj]):
                    shortest[idx_adj]=cand_shortest_adj
                    heappush(pq,(cand_shortest_adj,next))

# floyd - warshall
