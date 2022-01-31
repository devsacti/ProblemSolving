# summary

# comprehension

# utilizations and integration of datastructure-algorithms

# implementation
from collections import deque

# global

n,k=-1,-1

# bfs
def move(graph,s,visited,info_map):
    q=deque()
    
    stdR,stdC=s
    visited[stdR][stdC]=1
    info_map[stdR][stdC]='*'
    
    cost=0
    q.append((stdR,stdC,cost))
    
    # unit direction vector to desc position vector
    # 상하좌우
    dirs=[(0,-1),(0,1),(-1,0),(1,0)]
    
    while q:
        nowR,nowC,nowCost=q.popleft()
        # print(nowR,nowC)
        
        if(graph[nowR][nowC]!=0):
            # k보다 크면 방문을 못하니, 아랫 탐색에서 체크
            
            if(graph[nowR][nowC]==k):
                info_map[nowR][nowC]='.'
            
            if(graph[nowR][nowC]<k):
                info_map[nowR][nowC]=nowCost
      
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
              
              # assigning -1 on visited means unvisited and bigger
              visited[nr][nc]=-1
              info_map[nr][nc]='X'

              continue
            
            if(visited[nr][nc]==0):
              visited[nr][nc]=1
              q.append((nr,nc,nowCost+1))
              
if __name__=="__main__":
    n,k = map(int, input().split())
    
    # 2d matrix
    war_map=[]
    info_map=[[0]*n for _ in range(n)]
    
    for _ in range(n):
        row=list(map(int,input().split()))
        war_map.append(row)
    
    for r in range(n):
        for c in range(n):
            if(war_map[r][c]==9):
                stdR,stdC=r,c

    visited=[[0]*n for _ in range(n)]
    
    move(war_map,(stdR,stdC),visited,info_map)
    
    # print(*visited,sep='\n')
    # unvisited to -1 in war_map
    for r in range(n):
        for c in range(n):
            if(visited[r][c]==0):
              info_map[r][c]=-1
    
    for row in info_map:
      print(' '.join(map(str,row)))