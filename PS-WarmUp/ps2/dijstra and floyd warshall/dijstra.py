# summary

## reference

# PS
## comprehension
## problem
## shortest between v and v
## dijstra를 이해할 때, 아래와 같이
## 임의의 목표 now vertex를 상정하고 이에 접근 가능한 2개 이상의 prev vertex들, 
## 그리고 인접한 next vertex들을 상상하면 이해하기 좀더 편함

##
##    o ; prev1
##         o ; now vertext
## o ; prev2
##                 o ; next
##

## in & out condi
## n,m ; cnt of vertex, edge, int

## print dist from start to end

## utils & Integration of Algorithms

## heapq and idea of dp

## implementation
from collections import defaultdict
from heapq import *

def dijstra(graph, s, shortests):
    # 최초 시작 노드를 목적지로 이해할때
    # 즉, 목적지 이자 시작지점으로 이해할때, 둘이 같을 때 최단거리는 0이다.
    shortests[s]=0
    pq=[]
    heappush(pq,(0,s))
    
    # now까지 최단거리 후보들을 평가한 뒤 now 기준 next의 최단거리를 도출하는 과정이다.
    # next가 now되면 이는 최단거리로서 활용된다
    while pq:
        # 최초 시작점의 경우, 위 (0,s)가 heappop 되므로
        # 아래의 cand_shortest가 다소 혼란이온다. 왜냐하면 시작점은 prev vertex가 존재하지 않으니까,
        # 그렇다면 점화식에서 n-1과 n번째의 관계로 이해하면 좋지만
        # 익숙하지 않다면, 시작점도 주어지지 않았을 뿐, 여러 경로로 접근가능하다고 상상한다.
        # 마치 무대에 오르는 계단이 2개라고 생각하듯이

        # 그렇다면 무대에 오르는 계단이 1개는 바로 올라가서 거리가 0이고, 나머지는 1000이라 위의 초기화를 0으로 했다고 이해할 수 있다.

        # 이전 탐색을 통해 도출한 현재 지점까지의 최단거리 후보와 현재 노드
        cand_shortest,now=heappop(pq)
        
        # 어느정도 dijstra가 진행되었을때, now vertext를 2개의 vertex를 통해 접근가능한 상황을 처리하기 위함으로 생각하면 좋다
        ##
        ##    o ; prev1
        ##         o ; now vertext
        ## o ; prev2
        ##                 o ; next1
        ##                     o ; next2
        ##
        ## prev1을 통해 이미 shortests가 갱신된 후, prev2에서 now를 접근한다면, 아래 if문을 통해서 건너뛴다.
        if(cand_shortest>shortests[now]):continue

        # 위 if문을 통과함으로서 now까지의 최단거리로서 인정받은 것이고,
        # 이제는 이 now까지의 최단거리를 바탕으로 adjacent next의 최단거리를 선별 및 도출하는 과정
        for adj in graph[now]:
            interval, next = adj
            # 지금까지 온 거리이자 최단거리 + 다음 인접 노드까지의 거리로 adjacent next vertext 현상태의 유효한 최소값 정의
            # 다만 앞서 말한 위와같은 노드들 간 관계로, 상단 if를 통해 속아질수있다.
            shortest_adj=shortests[now]+interval
            
            if(shortest_adj<shortests[next]):
                # if문 안에 들어온 순간 adjacent next의 cand_shortest는 shortest 확정
                shortests[next]=shortest_adj
                heappush(pq,(shortest_adj,next))


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