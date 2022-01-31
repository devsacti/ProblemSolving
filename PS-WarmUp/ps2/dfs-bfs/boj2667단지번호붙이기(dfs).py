'''
reference : https://www.acmicpc.net/problem/2667

ps1. comprehension
ps1.1. analysis
n*n의 정사각형
0 based indexing 

ps1.2. drawing pattern, exception
2차원 매트릭스를 그래프로 이해
=> 모든 노드를 방문하면서, 아파트 노드에 대해선 인접노드를 확인하여, 노드들로 구성된 단지를 도출

ps2. applying computer algorithms
ps2.1. utilization
module 1 : 인풋값 2차원 리스트화, 아파트 단지를 표시할 상응 매트릭스 선언
module 2 : dfs를 통한 순회와 아파트 단지 표기, 

!! 이때 dfs 1번 호출 당, 아파트 플래그 넘버는 일정해야한다 => 외부로부터 constant한 값을 사용하는 방식이 적절하다고 생각(전역변수) 왜냐하면 호출마다 변동하는 게 아니라 일정해야하니까
!! 한편, cnt_node는 dfs 호출당 증가하는 변수임, 이는 recursive의 depth 변수처럼 이해하고, 이와같이 함수를 구성한다.
=> 하지만, 문제는 가변적인 limit을 가지고있어서, 여차저차 일단 global로 선언

module 3 : 아파트 단지 수와 단지별 노드 수 출력

!! 단지 수는 오름차순으로 출력

ps2.2. integration with Time complexity
module 1,2,3 

ps3. Impl
'''

# module 2
def dfs(now):
    global graph,visited
    global idx_flag, cnt_node,n
    # print(now)
    r_now,c_now=now
    visited[r_now][c_now]=idx_flag
    
    # print(*visited,sep='\n')
    # module1에서 매트릭스값이 1인 경우에 한하여 작동하게 설정하였으므로, 바로 카운팅
    cnt_node+=1
    # checking adjs
    adjs=[]

    # 상하좌우
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    for idx_dir in range(len(dr)):
        r_cand=r_now+dr[idx_dir]
        c_cand=c_now+dc[idx_dir]

        if(r_cand>(n-1) or r_cand<0 or c_cand>(n-1) or c_cand<0):
            continue

        if(graph[r_cand][c_cand]==0):
            continue

        # now candidates become valid adj
        adjs.append((r_cand,c_cand))
    
    for adj in adjs:
        r_adj, c_adj = adj
        if(visited[r_adj][c_adj]==0):
            now=(r_adj,c_adj)
            dfs(now)

    
    
if __name__=="__main__":    
    # module 1
    global n
    n=int(input())
    # 개인적으로 다른 함수가 쓸수도 있는 변수들은, 그리고 문제 상황에 대한 변수들은 글로벌이 더 적절한듯느껴지기 시작함
    
    global graph,visited
    graph=[list(map(int,list(input()))) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]

    # 아파트 정점에 한하여 flag값을 저장한 flag matrix를 별도 선언할수있지만,
    # 기능 상 visited에 1 대신 flag값을 할당하는것으로 통합가능하여 선언안함
    # graph_aparts=[[0]*n for _ in range(n)]

    # print(*graph,sep='\n')
    
    global idx_flag, answers
    idx_flag=0
    answer=[]

    token_new_set=False
    cnt_node=0

    for r in range(n):
        for c in range(n):
            # 아파트에 한하여 dfs 작동
            if(graph[r][c]==1 and visited[r][c]==0):
                # dfs 방식상 단지의 1개의 아파트라도 만나면 나머지도 모두 체크되므로, 프로세스 관점에선 1개의 아파트는 1개의 단지로 매칭될 수있다.
                idx_flag+=1
                cnt_node=0
                now=(r,c)
                dfs(now)
                answer.append(cnt_node)
    
    # print(*visited,sep='\n')
    
    answer.sort()
    print(idx_flag)

    for cnt in answer:
        print(cnt)