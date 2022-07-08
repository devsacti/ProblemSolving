# base
from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline

aparts=defaultdict(list)
apartKey=1

def bfs(graph,s,visited,apartKey):
  q=deque()
  q.append(s)
  
  # direction vector : up, down, left, right
  # magnitude = 1
  dr=[-1,1,0,0]
  dc=[0,0,-1,1]
  
  findNewSetToken=False
  
  while(q):
    #now
    r,c=q.popleft()

    #make adjs at 4 way; regard matrix as n*n graph
    adjs=[]
    for i in range(4):
      candR=r+dr[i]
      candC=c+dc[i]
      
      if(candR>(n-1) or candR<0 or candC>(n-1) or candC<0):
        continue
      
      adjs.append((candR,candC))
    
    for adj in adjs:
      if(visited[adj[0]][adj[1]]==0):
        # plus condition
        if(graph[adj[0]][adj[1]]==1):
          aparts[apartKey].append(adj)
          visited[adj[0]][adj[1]]=1
          q.append(adj)
          
          findNewSetToken=True
        else:
          continue
      else:
        continue

  return findNewSetToken

if __name__=="__main__":
  n=int(input().rstrip())
  graph=[list(map(int,list(input().rstrip()))) for _ in range(n)]
  visited=[[0]*n for _ in range(n)]
  main_findNewSetToken=False
    
  for r in range(n):
    for c in range(n):
      main_findNewSetToken=bfs(graph,(r,c),visited,apartKey)
      if(main_findNewSetToken):
        apartKey+=1
  # print('--')
  # for row in visited:
  #   print(row)
  print(len(aparts.keys()))
  result=[]
  for v in aparts.values():
    result.append(len(v))
    
  result=sorted(result)
  for item in result:
    print(item)