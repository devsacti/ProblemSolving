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
module 2 : bfs를 통한 순회와 아파트 단지 표기, 이때 bfs 1번 호출 당, 아파트 플래그 넘버는 일정해야한다 => 외부로부터 constant 아규먼트를 받는 것이 편리
module 3 : 아파트 단지 수와 단지별 노드 수 출력

!! bfs의 visited를 willbevisited로 설계했다면, 일련의 작업들도 미래에 할일로서 할당해야 로직이 안꼬임

!! 단지 수는 오름차순으로 출력

ps2.2. integration with Time complexity
module 1,2,3 

ps3. Impl
'''
from collections import deque

# module 2
def bfs(graph,visited,start,graph_aparts,idx_flag):
    r_start,c_start=start
    visited[r_start][c_start]=1
    q=deque()
    q.append(start)

    # 새로운 아파트 단지를 발견 시_방문 안한 노드가 1인 경우_, True로 전환,리턴, 이를 통해서 아파트 단지 넘버를 올린다.
    tmp_token_new_set=False
    # 새로운 아파트 단지의 노드수
    tmp_cnt_node=0

    # direction unit vector : up, down, left, right
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    # magnitude is 1, so abbr
  
    while(q):    
        # row and col of now
        r_now,c_now=q.popleft()

        # when now is node of apart, find valid adjs at 4 way; regard matrix as n*n graph
        if(graph[r_now][c_now]==1):
            # 현재가 아파트 노드인 동시에, flag가 없다면 새로운 아파트 단지
            if(graph_aparts[r_now][c_now]==0):
                tmp_token_new_set=True
                graph_aparts[r_now][c_now]=idx_flag

            tmp_cnt_node+=1

            adjs=[]
            for i in range(len(dr)):
                r_cand=r_now+dr[i]
                c_cand=c_now+dc[i]
              
                if(r_cand>(n-1) or r_cand<0 or c_cand>(n-1) or c_cand<0):
                    continue

                if(graph[r_cand][c_cand]==0):
                    continue
              
                adjs.append((r_cand,c_cand))
            
            # 상단에서 방문노드별로 인접노드 저장하면, 인접리스트로 구현된 그래프 생성가능      
            
            for adj in adjs:  
                r_adj, c_adj = adj
                if(visited[r_adj][c_adj]==0):
                    if(graph[r_adj][c_adj]==1):
                        # 로직상 최초 아파트단지 시작노드와 연결된 순간 플래그를 미리 꽂아놔야,
                        # 다른 아파트 단지의 최초 시작 노드와 구분된다.
                        graph_aparts[r_adj][c_adj]=idx_flag
                        visited[r_adj][c_adj]=1
                        q.append(adj)

    return tmp_token_new_set,tmp_cnt_node

if __name__=="__main__":
      # module 1
      n=int(input())
      graph=[list(map(int,list(input()))) for _ in range(n)]
      graph_aparts=[[0]*n for _ in range(n)]
      visited=[[0]*n for _ in range(n)]

      # print(*graph,sep='\n')
      # print(*graph_aparts,sep='\n')

      idx_flag=1

      token_new_set=False
      cnt_node=0

      answer=[]
      for r in range(n):
          for c in range(n):
              token_new_set,cnt_node=bfs(graph,visited,(r,c),graph_aparts,idx_flag)
              if(token_new_set):
                  answer.append(cnt_node)
                  idx_flag+=1

      # print(*graph_aparts,sep='\n')
      
      answer.sort()
      print(idx_flag-1)
      for cnt in answer:
        print(cnt)