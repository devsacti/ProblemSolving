# summary

## reference

# PS
## comprehension
## problem
## shortest between v and v
## dijstra를 이해할 때, 임의의 목표 now vertex를 상정하고 이에 접근 가능한 2개 이상의 이전 vertex들, 그리고 인접한 next vertex들을 상상하면 이해하기 좀더 편함

## in & out condi
## n,m ; cnt of vertex, edge, int

## print dist from start to end

## utils & Integration of Algorithms

## heapq and idea of dp

## implementation
from collections import defaultdict
from heapq import *

def dijstra(graph, s, shortests):
    shortests[s]=0
    pq=[]
    heappush(pq,(0,s))
    
    # now까지 최단거리 후보들을 평가한 뒤 now 기준 next의 최단거리를 도출하는 과정이다.
    # next가 now되면 이는 최단거리로서 활용된다
    while pq:
        # 이전 탐색을 통해 도출한 현재 지점까지의 최단거리 후보와 현재 노드
        cand_shortest,now=heappop(pq)
        
        # 문제는 최초의 노드_v0_에서 인접노드들_가령, v1,v2_로 접근할때, 인접노드들 간에 연결 되어있을 수 있다는 것이다.
        # 이 때 최초 노드에서 업데이트한 최단거리_v0 에서 v1_가 v2에서 v1으로 접근할때 최단거리보다 작다면, 최단거리로서 가치가 없고
        # 이를 제대로 예외처리하지 않는다면, 추후 최단거리 산출에서 오차가 생기므로 이렇게 스킵한다.
        if(cand_shortest>shortests[now]):continue

        # 위 if문을 통과함으로서 now까지의 최단거리로서 인정받은 것이고,
        # 이제는 이 now까지의 최단거리를 바탕으로 adjacent next의 최단거리를 도출하는 과정
        for adj in graph[now]:
            interval, next = adj
            # 지금까지 온 거리이자 최단거리 + 다음 인접 노드까지의 거리로 adjacent next vertext 최소 후보값 정의
            cand_shortest=shortests[now]+interval
          
            if(cand_shortest<shortests[next]):
                # if문 안에 들어온 순간 adjacent next의 cand_shortest는 shortest 확정
                shortests[next]=cand_shortest
                heappush(pq,(cand_shortest,next))


if __name__=="__main__":
    global graph,shortests
    n,m=map(int,input().split())
    
    inf=int(1e10)  
    
    graph=defaultdict(list)
    
    for _ in range(m):
        v1, v2 = map(int, input().split())
      
        # (interval between start and destination, dest vertex)
        graph[v1].append((1,v2))
        graph[v2].append((1,v1))
    
    s,e =map(int,input().split())
    
    # for k in sorted(list(graph)): 
    #   print(k,graph[k])
      
    shortests=[inf for _ in range(n)]
    
    dijstra(graph,s,shortests)
    
    print(shortests[e])