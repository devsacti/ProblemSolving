# 커스터마이징 부분, 티켓의 갯수를 통해서 순회를 조절하라, visited로는 한계
# 아에 visited를 제외해야한다.

# 관점의 전환, bruteforce와 그래프

def dfs(graph,v,visited,ticketCountMatrix,answer):
    # print('in dfs',v,answer)
    # print(*ticketCountMatrix,sep='\n')
    
    visited[v]=1
    answer.append(v)
    
    if(len(graph[v])>0):
        for adj in graph[v]:
            if(ticketCountMatrix[v][adj]>0):
                ticketCountMatrix[v][adj]-=1
                dfs(graph,adj,visited,ticketCountMatrix,answer)
                
            else: continue
                
def solution(tickets):
    answer = []
    
    places=[]
    
    for ticket in tickets:
        for place in ticket:
            if(place not in places): places.append(place)
    places.sort()
    # print(places.sort())
    
    n=len(places)
    idxs=[i for i in range(n)]
    place_idx={place : idx for place,idx in zip(places,idxs)}
    idx_place={idx : place for place,idx in place_idx.items()}
    # print(place_idx)
    # print(idx_place)
    
    graph=[[] for _ in range(n)]
    visited=[0 for _ in range(n)]
    
    ticketCountMatrix=[[0]*n for _ in range(n)]
    for ticket in tickets:
        place1, place2 = ticket
        
        node1, node2 =place_idx[place1],place_idx[place2]
        # print(node1, node2)
        graph[node1].append(node2)
        # 알파벳순방문을 위한 정렬
        graph[node1].sort()
        # print('adj list',graph[node1])
        
        ticketCountMatrix[node1][node2]+=1
    # print()
    # print(*graph,sep='\n')
    # print()
    # print(*ticketCountMatrix,sep='\n')
    # print()
    start="ICN"
    dfs(graph,place_idx[start],visited,ticketCountMatrix,answer)
    # print(answer)

    for place in places:
        if(visited[place_idx[place]]==0):
            dfs(graph,place_idx[place],visited,ticketCountMatrix,answer)
    
    answer2=[]
    for idx in answer:
        answer2.append(idx_place[idx])
    # print(answer2)
    
    return answer2