from collections import deque
import sys
input=sys.stdin.readline
# findHole
# delete cheeze except hole
# repeat

# plus to optimize
# Think based on cheeze

global dr,dc
dr=[-1,1,0,0]
dc=[0,0,-1,1]

# bfs for find exposed cheeze, based on standard out coord
def findExposed(matrix,s,visited):
  q=deque()
  visited[s[0]][s[1]]=1
  q.append(s)
  
  exposed=[]
  
  while(q):
    now=q.popleft()
    # now row, column
    nowr,nowc =now
    
    adjs=[]
    for i in range(4):
      # adjacent row, column
      adjr=nowr+dr[i]
      adjc=nowc+dc[i]
      
      if(adjr>(m-1) or adjr<0 or adjc>(n-1) or adjc<0):
        continue
      
      if(matrix[adjr][adjc]==1 and visited[adjr][adjc]==0):
        visited[adjr][adjc]=1
        exposed.append((adjr,adjc))
        continue
      
      adjs.append((adjr,adjc))
      
    for adj in adjs:
      adjr,adjc=adj
      if(visited[adjr][adjc]==0):
        visited[adjr][adjc]=1
        q.append(adj)
    
    
  return exposed

if __name__=="__main__":
  m,n=map(int,input().split())
  matrix=[list(map(int,input().split())) for _ in range(m)]

  # print(*matrix,sep='\n')
  
  # div0 simulation by while ; repeat (find cheeze, find inside)
  startToken=True
  time=0
  records=[]
  while(startToken):
    # use matrix as init, by the way init the visited
    visited=[[0]*n for _ in range(m)]
    exmatrix=[]
    
    exposedCheeze=findExposed(matrix,(0,0),visited)
    
    lengthCheeze=len(exposedCheeze)
    if(lengthCheeze==0):
      break

    # time start cuz there is exposed and excute
    time+=1
    cntCheeze=0
    for r in range(m):
      for c in range(n):
        if(matrix[r][c]==1):
          cntCheeze+=1
    records.append(cntCheeze)      
    
    for i in range(lengthCheeze):
      piece=exposedCheeze[i]
      r,c=piece
      matrix[r][c]=0
    
  print(time)
  print(records[-1])