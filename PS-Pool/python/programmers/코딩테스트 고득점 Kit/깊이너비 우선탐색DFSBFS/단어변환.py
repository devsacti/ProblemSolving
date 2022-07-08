# ps1. comprehension
# 1글자 변경 시 동일해지는 단어를 서로 인접노드로 이해하자
# 양방향
# 최소 몇단계 => vertex 간거리가 1일때 dijstra
# 주어진 자료상 begin과 target이 word안에 언제나 있지 않므로 추가필요

# ps2. applying algorithms
# module 인접노드 판별
# bfs extension ; dijstra

# 단어의 길이는 모두 같다

# ps3. impl
from collections import defaultdict
# from collections import deque
from heapq import *

def check(std,experi):
    cnt_differ=0
    token_adj=True
    
    # 단어의 길이는 모두 같다
    for idx in range(len(std)):
        if(std[idx]==experi[idx]):
            continue
        else:
            cnt_differ+=1
            
            # 2개 이상부터는 관심사가 아니다.
            if(cnt_differ==2):
                token_adj=False
                break
    
    return token_adj

def dijstra(graph,s,shortests):
    shortests[s]=0
    pq=[]
    heappush(pq,(0,s))
    
    while pq:
        cand_shortest_now, now = heappop(pq)
        print(cand_shortest_now, now)
        
        if(cand_shortest_now>shortests[now]):
            continue
        
        for adj in graph[now]:
            interval, next = adj
            shortest_adj=shortests[now]+interval
            
            if(shortest_adj<shortests[next]):
                shortests[next]=shortest_adj
                heappush(pq,(shortest_adj,next))
    
        
def solution(begin, target, words):
    answer = 0
    
    # begin이 words 내 없으나 graph화를 위해 추가
    if begin not in words:
        words.append(begin)
    
    graph=defaultdict(list)
    # visited={key:0 for key in words}
    inf=int(1e3)
    shortests={key:inf for key in words}

    
    for word_std in words:
        for word_experi in words:
            if word_std==word_experi:
                continue
            else:
                if(check(word_std,word_experi)):
                    graph[word_std].append((1,word_experi))
    
    # for key,val in graph.items():
    #     print(key,val)
    
    # dijstar를 통한 최단거리(최소 몇단계 ) 도출
    s=begin
    dijstra(graph,s,shortests)
    # print(shortests)
    
    if target in shortests.keys():
        answer=shortests[target]
    else:
        answer=0
    
    return answer