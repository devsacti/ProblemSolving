# https://www.acmicpc.net/problem/1991

# ps1. comprehension
## A is root node

# ps2. applying computer algorithms

# ps3. impl
# 전위는 현재 방문노드, lc, rc
# 중위는 lc, 현재 방문노드, rc
# 후위는 lc, rc, 현재 방문노드 로 print()의 우선순위를 가진다고 생각하자

# 한편 root를 기준으로 전위는 처음이 root, 후위는 마지막이 root이다.

from collections import defaultdict

def recursive_pre(tree,v):
    adjs = tree[v]
    lc,rc=adjs

    print(v, end='')
    if(lc !='.'):
        recursive_pre(tree,lc)

    if(rc !='.'):
        recursive_pre(tree,rc)


def recursive_inorder(tree,v):
    adjs = tree[v]
    lc,rc=adjs

    if(lc !='.'):
        recursive_inorder(tree,lc)
    print(v, end='')
    if(rc !='.'):
        recursive_inorder(tree,rc)

def recursive_post(tree,v):
    adjs = tree[v]
    lc,rc=adjs

    if(lc !='.'):
        recursive_post(tree,lc)
    if(rc !='.'):
        recursive_post(tree,rc)
    print(v, end='')


if __name__=="__main__":
    n=int(input())

    tree=defaultdict(list)

    for _ in range(n):
        parent,lc,rc=input().split()

        # left child 부터 append
        tree[parent].append(lc)
        tree[parent].append(rc)

    # for key, val in tree.items():
    #     print(key, val)

    recursive_pre(tree,'A')
    print()
    recursive_inorder(tree,'A')
    print()
    recursive_post(tree,'A')