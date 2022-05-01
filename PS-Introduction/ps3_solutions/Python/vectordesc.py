from collections import defaultdict

# make valid adjs by vector=dr*magnitude
dir_adjs=defaultdict(list)

for i in range(1,4+1):
    for magnitude in range(1,3+1):
        # candidate row, column
        cand_r=now_r+dr[i]*magnitude
        cand_c=now_c+dc[i]*magnitude
        
        if(cand_r>(m-1) or cand_r<0 or cand_c>(n-1) or cand_c<0):
          break
        
        if(matrix[cand_r][cand_c]==1):
          break
        
        # candidate becomes valid
        dir_adjs[i].append((cand_r,cand_c,i))