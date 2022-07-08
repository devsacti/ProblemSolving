'''
ps1.comprehension
    주어진 항공권을 모두 이용할것!
    
ps2.applying computer algorithms
    recursive and backtracking => 주어진 항공권을 모두 이용하고 방문지를 저장
    
ps3.impl

'''
from collections import defaultdict

# dfs for traversing directed graph
# global ; graph

# 일단 비행기표가 있다는 것은 다음 행선지로서 자격을 의미
# 하지만 모든 비행기표를 써야하는 상황에서 행선지에 도착했을때 여전히 다른 비행기표가 남아있다면
# 그것은 unpromising으로 판단

# ? 하지만 a -> b -> c -> d 에서 d가 unpromising한건 알고, c로 back했지만 
# 알고보니 b까지 back한다음 a -> b -> e -> c- > d를 가야한다면 어떻게하지..
# 우선은 unpromising 조건을 더 상세화해야 겠지만, 좀 오래 봐야할듯
def promisiong():
    pass

def recursive(now,len_tickets):
    visited[now]=1
    answer.append(now)
    
    for adj in graph[now]:
            
        if valid_cnt_ticket[now][adj] > 0:
            valid_cnt_ticket[now][adj]-=1
            len_tickets-=1
            dfs(adj,len_tickets)

def solution(tickets):
    global graph,visited
    global valid_cnt_ticket
    global answer
    global len_tickets
    
    graph=defaultdict(list)
    visited=defaultdict(int)
    len_tickets=len(tickets)
    # print(len_tickets)
    answer=[]
    
    for ticket in tickets:
        v1,v2 = ticket
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 오름차순을 위한 정렬
    
    for key in graph:
        graph[key].sort()
        
    # dict
    valid_cnt_ticket = defaultdict(dict)
    
    vertexes = list(graph)
    
    # dict shellow copy로 인해 새로 행 선언과 동시에 할당
    for vertex in vertexes:
        valid_cnt_ticket[vertex]= {v : 0 for v in vertexes}
    
    # for key,val in valid_cnt_ticket.items():
    #     print(key,val)
    # print()
    
    for ticket in tickets:
        v1,v2 = ticket
        valid_cnt_ticket[v1][v2]+=1
    
    for key,val in valid_cnt_ticket.items():
        print(key,val)
    # print(graph)
    dfs('ICN',len_tickets)
    # print(answer)
    
    return answer