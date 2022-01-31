'''
reference link : https://www.acmicpc.net/problem/1238

ps1 comprehension about problem
ps1.1. analysis

모든 학생들은 집에서 x에 갈 수 있다.

ps1.2. drawing pattern, exception

pattern1.
pattern of dijstra

ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing

module 1 : dijstra

ps2.2. integrations

ps3. Impl
'''
from collections import defaultdict
import heapq

# module 1
def dijstra(s,shortests):
    global graph
    shortests[s]=0
    pq=[]
    heapq.heappush(pq,(0,s))

    while pq:
        cand_shortest,now=heapq.heappop(pq)
        # now까지 최단거리로서 가치가 있나없나 체크, 없다면 continue
        if(cand_shortest>shortests[now]):
            continue
        
        # 있다면, 다음 행선지까지의 최단거리 후보를 제공할 수 있으므로, 인접 노드 방문
        for adj in graph[now]:
            interval, next=adj
            cand_shortest=shortests[now]+interval

            if(cand_shortest<shortests[next]):
                shortests[next]=cand_shortest
                heapq.heappush(pq,(cand_shortest,next))
    
    return shortests

if __name__=="__main__":
    n,m,x=map(int,input().split())
    end=x
    global graph
    graph=defaultdict(list)
    
    inf=int(1e20)

    for _ in range(m):
        v1,v2,cost = map(int, input().split())

        graph[v1].append((cost,v2))

    keys=sorted(list(graph))
    # for key in keys:
    #     print(key,' ',graph[key])

    max_distance=-1
    for start in range(1,n+1):
        go_back_dist=0
        if(start==end):
            go_back_dist=0
        else:
            # print(start,end)
            # start to end
            shortests=[inf for _ in range(n+1)]
            shortests=dijstra(start,shortests)
            go_back_dist+=shortests[end]
            # print(shortests)

            # end to start
            shortests=[inf for _ in range(n+1)]
            shortests=dijstra(end,shortests)
            go_back_dist+=shortests[start]
            # print(shortests)

        max_distance=max(go_back_dist,max_distance)
    print(max_distance)