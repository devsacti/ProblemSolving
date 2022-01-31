from collections import defaultdict

# make valid adjs by vector=dr*magnitude
dir_adjs=defaultdict(list)

for i in range(1,4+1):
  for magnitude in range(1,3+1):
    # candidate row, column
    candR=nowR+dr[i]*magnitude
    candC=nowC+dc[i]*magnitude
    
    if(candR>(m-1) or candR<0 or candC>(n-1) or candC<0):
      break
    
    if(matrix[candR][candC]==1):
      break
    
    # candidate becomes valid
    dir_adjs[i].append((candR,candC,i))