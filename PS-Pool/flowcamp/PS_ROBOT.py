# 1.problem reference
#  algorithmjobs lms

# 2.core algorithm, language
#  dijstra
#  !! dijstra에는 dp와 bruteforce가 내재되어있었다~!
#  python

# 3.time complexity

# 4. ps ; accuracy, utilizing&Integrating algorithm, implementation

# AC
#  객체와 액션!! 객체뿐만아니라 개별 액션(또는 규칙)에 대해서도 대응하는 알고리즘이 최소 필요, 건너띌 생각 ㄴㄴ
#  2d matrix, robot

#  ! Not computer index
#  최소 몇번의 명령=> 최단거리와 최소 명령어 판별, 
#  우선 최단거리를 만족하는 경로들을 구해야함, 이때 시작점을 기준으로하면 복잡,
#  우선 bfs로 거리 찍고, 목표점에서 시작점으로 거슬러 올라가는 형태로 최단거리로 돌아가는 길을 찾아야함
#  !!comment1 근데 이게 1칸씩 이동가능하면 그런데, 생각해보니까 거리 상으로는 멀어도, 3칸 단위의 이동이 가능하기 때문에 명령어횟수는 적을 수 있음....
#  !! 이런 점에서 시작점에서 목표점으로의 모든 경로를 구하면 되니까, 따로 bfs로 최단거리만 따질게 아니였음
#  !! 결국은 다익스트라인데 인접노드를 4방면 외에도 1,2,3으로 해서 모든 경우를 따지면 최소명령어로 접근가능할듯

# - 이상적으론 방향전환을 최소화하면서 3칸씩 이동하면 최소 명령어이다.다만, 어느 길이 최소의 방향전환&큼직한 이동을 보장하는지 모른다
# - 1턴에 반드시 이동 혹은 방향전환을 한다.

# ? 벽이 없다면 이라는 접근은 어떨까, 벽이 없을때의 경로에서 변형?

# comment1
# 3 4 5 6 7 8
# 2 b b b b 9
# 1 2 3 4 b 10
# s 1 b 5 6 e

# 거리기준 접근
# 9번

# 그러나, 거리기준으로는 10이나, 3칸이동횟수가 많은 길은,
# 시작과 끝지점의 방향을 거리기준 접근에 유리하게 해도,
# 8번

# CA
#  최적의 경로에 대한 패턴을 못찾음
#  bfs로 브루트포스하게 경로를 구한다.
#  !! 벡터의 d와 m을 제어하라
#  !! 단, 발생하는 경우마다 visited를 줘서 경로별 독립성을 부여하되, 과부하를 막기 위해 전역변수로 최소 명령어수를 선언해서 이 값보다 커지면 경로탐색을 종료

#  visited와 관련해서 이 경우 최소 명령어를 요구하므로, 처음 접근할때, 현재좌표와 현재방향을 고려해서 최소로 접근하면 다른 방면의 접근은 굳이 고민하지 않아도 된다.
#  즉, 백트래킹으로서 가치가 있다.
# IM

# !! 벡터 다루기
# 기본적으로 유닛벡터*magnitude로 접근하면
# 현재 방향은 유닛벡터 인덱스와 비교해서 magintude상관없이 방향속성만 판단가능

# Analysis of ROBOT
# bfs로 공간별 최단거리 구한 뒤, 1씩 차감되는 특징을 따라
# 역으로 '마치 산 정상에서 하강하듯이' 목적지에서 출발지로 되돌아가서 경로를 구한다.
# 
# 이 경로를 통해서 최소 커맨드 수를 구해본다.

# ? 최단경로가 2개 일때, 최소 커맨드 수가 다를까?
#=> 시작점과 도착점에서 회전수로 또 구분될듯

from collections import deque
from collections import defaultdict
INF=int(1e4)
#        동서남북 
#        1 2 3 4
dr=[None,0,0,1,-1]
dc=[None,1,-1,0,0]

# 문제가 되는 부분은 좌우회전 횟수가 0,2로 같은 0도 또는 180도가 아니라, 90도 
# 하지만 문제가 되는 부분을 하나하나 설정하면 너무 길어지니까, 깔끕한 애들을 설정, 마치 여집합
def getturncnt(nowD,nextD):
  if(nowD==nextD):
    return 0
  elif( (nowD==1 and nextD==2) or (nowD==2 and nextD==1) or (nowD==3 and nextD==4) or (nowD==4 and nextD==3)):
    return 2
  else:
    return 1

# robot ; bfs based
def robot(matrix,m,n,start,end,cntcmdmatrix):
  q=deque()
  # basic config
  # visited[start[0]][start[1]]=1
  cntcmdmatrix[start[0]][start[1]]=0
  # row, column, dir, cnt of cmd
  q.append((start[0],start[1],start[2],0))
  
  # plus config
  # end Row, end Column, end Dir
  eR,eC,eD = end[0], end[1], end[2]

  while(q):
    nowR, nowC,nowD, nowCnt = q.popleft()
    
    # for r in range(m):
    #   for c in range(n):
    #     if(r==nowR and c==nowC):
    #       print('*', end='')
    #     else:
    #       print(matrix[r][c],end='')
    #   print()
      
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
    
    if(nowCnt>cntcmdmatrix[nowR][nowC]): continue
        
    # print(dir_adjs)
    # 도출된 인접노드들에 대해서 후속처리, 고전적으로
    ks=list(dir_adjs)
    for i in range(len(ks)):
      k=ks[i]
      for adj in dir_adjs[k]:
        adjr,adjc,adjd = adj
        # cmdcnt=move cnt(=1) + turn cnt
        adjcnt=nowCnt+1+getturncnt(nowD,adjd)
        
        # arriving at destination
        if(adjr==eR and adjc == eC):
          # print('endpoint',cntcmdmatrix[adjr][adjc])
          adjcnt+=getturncnt(adjd,eD)
        
        if(adjcnt<cntcmdmatrix[adjr][adjc]):
          cntcmdmatrix[adjr][adjc]=adjcnt
          q.append((adjr,adjc,adjd,adjcnt))
    
    # print('--')
    # print(*cntcmdmatrix,sep='\n')
  
if __name__=="__main__":
  m,n = map(int,input().split())
  matrix=[list(map(int,input().split())) for _ in range(m)]
  
  start=list(map(int,input().split()))
  end=list(map(int,input().split()))
  # modification to INDEX OF COMPUTER
  start[0]-=1;start[1]-=1
  end[0]-=1;end[1]-=1
  
  # print('--')
  # print(*matrix,sep='\n')

  # print('--')
  # print(start,end)
  
  cntcmdmatrix=[[INF]*n for _ in range(m)]
  cmdlogdict=defaultdict(list)
  
  robot(matrix,m,n,start,end,cntcmdmatrix)
  print(cntcmdmatrix[end[0]][end[1]])