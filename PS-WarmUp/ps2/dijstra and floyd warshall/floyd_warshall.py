'''
ps1. comprehension
ps1.1. analysis
ps1.2. drawing pattern, exceptions

개인적으로 플로이드는 최단거리를 계산하기 시간복잡도가 너무 큰 그래프를 보고,
차라리 노드간의 직전 최단거리를 그어버리면 어떨까라는 생각을 했지 않을까한다.

하지만, 주어진 그래프를 왜곡할수는 없을 것이고, 그래서 생각해낸것이 '1점을 경유'한다는 것으로 생각된다.
우선 이것만으로도, 1점을 경우해서 접근 가능한 이웃 노드들의 최단거리는 도출가능해지나,

노드 간 겨우 1~2개의 간선만 존재하는 거미줄같은 그래프나 트리에서,
즉 한 노드에서 다른 노드로 최단거리로 가기위해선 2개이상의 수많은 노드들을 복잡하게 지나야하는 그래프에서

이것이 어떻게 작동가능한지 개인적으로 궁금했는데,
우선 이산적으로 간선이 1개에서 최대 2개인 복잡한 그래프는 잘 펼치고 정리하면 1줄로 연결된 트리에 불과하고,

1점을 경유해서 최단거리를 도출하는 접근은
가상으로 격리된 두 개의 노드를 연결하는 상상의 최단 거리 직선을 연결하는 행위로 이해할 수 있고,
이는 다른 노드 간 가상의 최단거리 직선과 독립적으로,
삼각형의 사이클을 만들어가는 것으로 이해가능하다.

그리고 이렇게 삼각형의 사이클을 만들다 보면 결국 모든 다각형은 3각형으로 분할가능하므로,
연결된 노드들 간에는 최단거리를 도출가능해지지 않나라고 이해해봤다.

하지만 역시나 스스로에게 충분히 와닿지 않는다. 
그러나 구현이 이제는 더 중요하므로, 차차 스스로의 의문과 관련된 예시를 만들어 해결해보자
그리고 구현하면서 다시 보면 또 되기도 하고

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
      n,m,k=map(int,input().split())

      inf=int(1e9)
      # for floyd-warshall
      global shortests
      shortests=[[inf]*n for _ in range(n)]

      for _ in range(m):
        v1, v2, cost = map(int, input().split())

        # 2d shortests
        shortests[v1-1][v1-1]=0
        shortests[v1-1][v2-1]=cost
        shortests[v2-1][v2-1]=0
      
      # print(*shortests, sep='\n') 

      floyd_warshall()

      total=0

      for s in range(n):
        total+=(shortests[s][k-1]+shortests[k-1][s])
      
      print(total)