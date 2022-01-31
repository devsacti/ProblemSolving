# 처음에는 graph 대신 words, v 대신 word로 해서 target에 해당하는 node 방문시 종료하는형태로 만들면 되겠다함, visited는 커스터마이징상 생략가능이라고 착각
# 그러나 dfs가 작동함에 있어 필수불가결한 visited가 필요했고, 내딴에는 커스터마이징이라고 생각한게 알고리즘상 필수였고
# 결국은 인덱싱이 필수였음
#

# 최단거리 개념이 들어가는 순간  원래는 다익스트라인데, 프로그래머스의 적은 테스트케이스상에서는
# 운좋게 dfs 첫번째 갈래에 하위갈래에 원하는 타겟이 있어서, 자동으로 최단거리값이 도출될 수 있었다.
# 그러나 원래 dfs만으론 단순히 '순회'이지 최단거리는 우연히 도출되는것이다.
from  collections import deque
import heapq
import sys
input=sys.stdin.readline

INF = int(1e9)
def dijkstra(graph,start,dist):
    pq=[];heapq.heappush(pq,(0,start))
    dist[start]=0

    while(pq):
        curDist,curNode = heapq.heappop(pq)

        if(dist[curNode]<curDist): continue

        for adj in graph[curNode]:
            cost= curDist+adj[1]

            if(cost<dist[adj[0]]):
                dist[adj[0]] = cost
                heapq.heappush(pq,(cost,adj[0]))

    return dist

def solution(begin, target, words):
    answer = 0

    if(begin not in words):
        words=[begin]+words
    # by indexing the word and regarding as node, i can make graph based on adj list
    graph=[]
    print(words)
    n=len(words)

    idxs=[i for i in range(n)]
    word_idx={word: idx for word,idx in zip(words,idxs)}
    idx_word={idx : word for word,idx in word_idx.items()}

    stdLen=len(begin)
    # checking adjacency and make graph
    for word in words:
        temp=words[:]
        # print(temp)
        temp.remove(word)
        # print(temp)

        adjList=[]
        for experi in temp:
            difference=0
            for idx in range(stdLen):
                if(word[idx]!=experi[idx]):
                    difference+=1
                    if(difference>1):break
                
            if(difference==1):
                adjList.append((word_idx[experi],1))

        graph.append(adjList)
                
    print(graph)
    dist=[INF for _ in range(n)]
    dist=dijkstra(graph,0,dist)
    print(dist)

    if(target in words): answer=dist[word_idx[target]]
    else: pass
    
    print(answer)
    return answer


begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin,target,words))