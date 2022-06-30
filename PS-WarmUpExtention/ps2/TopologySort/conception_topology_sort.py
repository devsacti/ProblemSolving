'''
Directed Acyclic DAG 가정

O(V+E)

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

'''
from collections import defaultdict
from collections import deque

def topology_sort(v):
    # print('##',v)
    q=deque()
    progress_move=[]

    for i in range(1,v+1):
        # print('###',indegree[i])
        if(indegree[i]==0):
            q.append(i)

    print(q)

    while q:
        now = q.popleft()
        progress_move.append(now)

        for adj in DAG[now]:
            indegree[adj] -= 1

            if(indegree[adj] == 0):
                q.append(adj)

    return progress_move

if __name__=="__main__":
    v,e=map(int,input().split())

    # indegree=defaultdict(int)
    DAG=defaultdict(list)
    indegree={k:0 for k in range(1,v+1)}

    for _ in range(e):
        v1,v2= map(int,input().split())

        DAG[v1].append(v2)
        indegree[v2]+=1

    # find start vertex whose indegree is 0
    for key,val in DAG.items():
        print(key ,val)

    print(indegree)

    print('#')
    Answer=[]
    Answer=topology_sort(v)

    print(Answer)