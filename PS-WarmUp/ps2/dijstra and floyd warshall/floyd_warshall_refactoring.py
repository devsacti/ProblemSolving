'''
link : https://www.acmicpc.net/problem/11404

ps1. comprehension
ps1.1. analysis
ps1.2. drawing pattern, exceptions
ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing
ps2.2. integration

ps3.Impl
'''
def floyd_warshall():
      global n,shortests

      for k in range(n):
            for s in range(n):
                  for e in range(n):
                        shortests[s][e]=min(shortests[s][e], shortests[s][k]+shortests[k][e])
      
      # print()
      # print(*shortests,sep='\n')


if __name__=="__main__":
      n = int(input())
      m = int(input())

      inf=int(1e9)
      # for floyd-warshall
      global shortests
      shortests=[[inf]*n for _ in range(n)]

      for _ in range(m):
        v1, v2, cost = map(int, input().split())

        # 2d shortests
        shortests[v1-1][v1-1]=0
        shortests[v1-1][v2-1]=min(cost,shortests[v1-1][v2-1])
        shortests[v2-1][v2-1]=0
      
      # print(*shortests, sep='\n') 

      floyd_warshall()

      for r in range(n):
            for c in range(n):
                  if(shortests[r][c]==inf):
                        print(0, end=' ')
                  else:
                        print(shortests[r][c],end=' ')
            print()