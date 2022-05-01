'''
ps1.comprehension
    주어진 항공권을 모두 이용할것!
    
ps2.applying computer algorithms
    단방향 구조상 visited는 생략 => ICN으로 다시 돌아가는 티켓있음, 단방향이지만 사이클 존재로 visited 필요
    => 다시 방문이 가능하기 때문에 visited보단 pop으로 처리
    => 우선 있는걸로 해결해보자, visitid를 used 처럼 생각
    => visited는 사용가능 횟수와 숫자 방향이 다름, 증가와 감소
    => pop으로 처리
    
    graph 접근은 좋았고, dfs도 좋은데, recursive에 더 가까운 상황이었다. dfs는 인접노드를 결국방문하지만, 이는 그저 목표지점까지의 recursive
    
    => 티켓만 있으면 양방향이었다.
    
ps3.impl



'''
from collections import defaultdict

# dfs for traversing directed graph
# graph,visited ; global
def dfs(now,len_tickets):
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