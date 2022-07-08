## template
from itertools import combinations
import copy
import sys
from collections import deque
input = sys.stdin.readline 
INF = float('inf')
# -----------------------------------------------
T = int(input())
for t in range(T):
  # -----------------------------------------------
  n, m, k = map(int,input().split())
  room = []
  for _ in range(n):
    room.append(list(map(int,input().split())))
  # -----------------------------------------------
  diffs = []
  empty_num = 0   ###########################
  for a in range(n):
    for b in range(m):
      if room[a][b] == 2:
        diffs.append((a,b))
      if room[a][b] == 0:
        empty_num += 1
  # -----------------------------------------------
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  def diffuse(room, comb):
    cnt = 0
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    for x, y in comb:
      dist[x][y] = 0
      q.append((x, y))
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and room[nx][ny] != 1 and dist[nx][ny] == -1 :
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx,ny))
          if room[nx][ny] != 2 :cnt += 1 #######################
    if cnt == empty_num:  ###########################
     return dist
    else:
      return -1
  # -----------------------------------------------
  result = INF
  combs = combinations(diffs,k)
  for comb in combs:
    dist = diffuse(room, comb)
    if dist != -1:
      time = 0
      for a in range(n):
        for b in range(m):
          if room[a][b] == 0:  ##################################
            time = max(time, dist[a][b])
      result = min(result, time)
  # -----------------------------------------------
  if result == INF:
    print('#'+str(t+1),-1)
  else:
    print('#'+str(t+1),result)