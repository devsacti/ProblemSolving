# summary

# comprehension

# utilizations and integration of datastructure-algorithms

# implementation
# war_map에 싸움가능한 적이 아무도 없으면 pq에서 리스트 인덱스 에러뜸 => 길이 체크 추가
from collections import deque
# global

n,k=-1,-1

# bfs
def search(graph,s,visited,info_map,pq):
    q=deque()
    
    stdR,stdC=s
    visited[stdR][stdC]=1
    info_map[stdR][stdC]='*'
    
    cost=0
    q.append((stdR,stdC,cost))
    
    # argument pq is priority queue
    # for record the priority of enemy, enemy is represented by its coord 
    
    # unit direction vector to desc position vector
    # 상하좌우
    dirs=[(0,-1),(0,1),(-1,0),(1,0)]
    
    while q:
        nowR,nowC,nowCost=q.popleft()
        # print(nowR,nowC)
        
        if(graph[nowR][nowC]!=0):
            
            # 현재 방문지가 
            # k보다 크면 방문을 못하니, 아랫 탐색에서 체크
            
            # k와 같은 경우, 적과의 만남만 가정
            if(graph[nowR][nowC]==k):
                info_map[nowR][nowC]='.'
                
            # k보다 작은 경우, 적과의 만남 가정과 싸움
            if(graph[nowR][nowC]<k):
                info_map[nowR][nowC]=nowCost
                # 우선순위의 독립변수는 거리 그 다음 y(=r) 그 다음 x(=c)
                # <WRONG>그리고 3가지 모두 양의 정수라 이들의 합으로 오름차순 우선순위 정의가능
                # 우선 nowCost만 비교,
                # 그런데도 같으며 '그 다음에' nowCost+nowR
                # 그런데도 같으면 '그 다음에' nowCost+nowR+nowC
                # 아래와 같이 세이브해서 추후 다중정렬
                pq.append((nowCost,nowCost+nowR,nowCost+nowR+nowC,nowR,nowC))
        
        # 주변 탐색 
        for dir in dirs:
            # magnitude는 1
            dr,dc=dir
          
            nr=nowR+dr
            nc=nowC+dc
          
            if(nr<0 or nr>n-1 or nc<0 or nc>n-1):
              continue
          
            if(graph[nr][nc]>k):
              # 최초시작점은 패스
              if(nr==stdR and nc==stdC): continue
              
              # assigning -1 on visited means 'unvisited and bigger'
              visited[nr][nc]=-1
              info_map[nr][nc]='X'

              continue
            
            if(visited[nr][nc]==0):
              visited[nr][nc]=1
              q.append((nr,nc,nowCost+1))
              
if __name__=="__main__":
    # under main, n,k is global
    n=int(input())
    k=2
    # n,k = map(int, input().split())
    
    # 2d matrix
    war_map=[]
    info_map=[[0]*n for _ in range(n)]
    
    for _ in range(n):
        row=list(map(int,input().split()))
        war_map.append(row)
    
    # init the stdR,stdC
    for r in range(n):
        for c in range(n):
            if(war_map[r][c]==9):
                stdR,stdC=r,c

    visited=[[0]*n for _ in range(n)]
    enemies=deque()
    
    # for init the priority_enemy li
    search(war_map,(stdR,stdC),visited,info_map,enemies)
    priority_enemy=deque(sorted(enemies,key=lambda enemy : (enemy[0],enemy[1],enemy[2])))
    # print(*visited,sep='\n')
    # print('--')
    
    # print('init info_map for while')
    # for row in info_map:
    #   print(' '.join(map(str,row)))
    # print('--')
    
    # print(priority_enemy)
    
    answer=0
    while priority_enemy:
        curTarget=priority_enemy.popleft()
        val1,val2,val3, targetR,targetC=curTarget
        dist=abs(stdR-targetR)+abs(stdC-targetC)
        answer+=dist
        stdR=targetR
        stdC=targetC
        # 0 means nothing and if soldier remove the enemy there is nothing
        war_map[stdR][stdC]=0
        
        # print('after hunt')
        # for row in war_map:
        #   print(' '.join(map(str,row)))
        # print('--')
        
        # re init and search for new info
        info_map=[[0]*n for _ in range(n)]
        visited=[[0]*n for _ in range(n)]
        enemies=deque()
        
        # updating info_map
        search(war_map,(stdR,stdC),visited,info_map,enemies)
        
        # sorting enemy based on condition
        priority_enemy=deque(sorted(enemies,key=lambda enemy : (enemy[0],enemy[1],enemy[2])))
        # for row in info_map:
        #   print(' '.join(map(str,row)))
        # print('--')
        
        # print(stdR,stdC)
        # print('--')
        # print(priority_enemy)
      
    print(answer)