'''
reference : ?

ps1. comprehension about problem
ps1.1 analysis
leaf 부터 inner node들을 거쳐 root node까지 이어지는 형태
leaf를 가진 부모노드의 weight는 그들 자식들의 weight의 합으로 정의
root node의 넘버는 1

주어진 물의 양이 트리에서 종합된 weight으로 나눠질때, leaf에 할당되는 양을 산출
단, 나눠지지 않으면 -1

ps1.2 drawing pattern ~ exceptions
child node의 weight를 1로 간주하여, parent node로 전파

ps2. utilizing and integration of computer algorithms
ps2.1. utilizing
module1 : from Vertex,edge,which is not directed, to graph to tree
module2 : finding leaf

!! 정형화된 조건에서 dfs는 recursive 기반 bruteforce로 이해가능하다.

module3 : propagate the weight of leaf to parent and sum the weight
module4 : estimate whether given water is divided by sum of weight

ps2.1. integration
module 1,2,3,4

ps3. Impl
'''
from collections import defaultdict
from collections import deque

# sub of module 1 by bfs, making trees from graph
def make_tree(graph,visited,s):
    # tmp for return
    tmp_tree=defaultdict(list)
    tmp_reversed_tree=defaultdict(list)
    
    visited[s]=1
    q=deque();q.append(s)
    
    while(q):
        now=q.popleft()
      
        for adj in graph[now]:
            if(visited[adj]==0):
                tmp_tree[now].append(adj)
                visited[adj]=1
                q.append(adj)
            else:
                tmp_reversed_tree[now].append(adj)
          
    return tmp_tree,tmp_reversed_tree
    
# module 2 graph dfs 순회를 통해서도 leaf를 찾을 수 있고, 큰 차이없으나 일단 트리
def find_leaf(tree, visited,now,leafs):
      # 방문처리
      visited[now]=1

      # 현 노드 방문처리 후, 전체를 다 돌았나 평가해야한다. 이걸 먼저 실행하면, 최종노드 방문 후 leaf node 평가가 안될 수 있다.
      # 전체 노드 방문 여부에 대해선, 방문 시 1이 할당되므로 visited의 총합으로 평가가능(0번노드의 값은 0이기도 하고)
      # 인덱싱을 1부터하기 위해 0번째를 붙였으므로, n 은 len(visited)-1로 표현가능
      # print(now, tree[now], visited)
      # if(sum(visited)==len(visited)-1):
      #     print('ck')
      #     return leafs
      # => 전체 노드를 다 돌면 자동으로 더이상 dfs가 call되지 않는다, 즉 이미 dfs는 전체 노드를 방문하는 순간 정지된다.
      # 별도의 if문 불필요, 구조상
      
      # leaf node인지 평가
      if(len(tree[now])==0 ):
          leafs.append(now)

      # 현재 노드 주변 탐색 recursive of dfs
      for adj in tree[now]:
          if(visited[adj]==0):
              leafs=find_leaf(tree, visited,adj,leafs)
              
      return leafs
      
# module 3 ; bfs based on reversed_tree
# tree 특성상 visited 불필요하나, 상기를 위해 기입
def propagatation_leaf(reversed_tree,s,visited,weights):
    visited[s]=1
    q=deque();q.append(s)
    
    while(q):
        now=q.popleft()
        
        for adj in reversed_tree[now]:
            if(visited[adj]==0):
                weights[adj]+=1
                
                visited[adj]=1
                q.append(adj)
    
    return weights

# module 4 ; estimate valid distribute or not, and if possible share
def estimate(water, sum_weight):
    if(water%sum_weight==0):
        return water//sum_weight
    else:
        return -1


if __name__=="__main__":
    # module 1
    n,water = map(int,input().split())
    
    # making graph
    graph=defaultdict(list)
    for _ in range(n-1):
        v1,v2=map(int,input().split())
      
        # because given edge has no direction information, make undirected graph
        graph[v1].append(v2)
        graph[v2].append(v1)
      
    key_graph=sorted(list(graph))
    
    # for key in key_graph:
    #     print(key,' ',graph[key])
    
    # making trees from graph
    tree=defaultdict(list)
    reversed_tree=defaultdict(list)
    idx_root=1
    visited=[0]+[0 for _ in range(n)]
    
    tree,reversed_tree=make_tree(graph,visited,idx_root)
    
    # print('#')
    # for idx in range(1,n+1):
    #     print(idx,' ',tree[idx])
    
    # print('#')
    # for idx in range(1,n+1):
    #     print(idx,' ',reversed_tree[idx])

  
    # module 2
    visited=[0]+[0 for _ in range(n)]
    now=1
    leafs=[]
    leafs=find_leaf(tree, visited,now,leafs)
    # print(leafs)
    
    # module 3
    weights=[0]+[0 for _ in range(n)]
    
    for leaf in leafs:
        weights[leaf]=1
        # print('leaf',weights)
        visited=[0]+[0 for _ in range(n)]
        weights=propagatation_leaf(reversed_tree,leaf,visited,weights)
    # print(weights)
    
    # module 4
    answer=estimate(water, sum(weights))
    
    print(answer)