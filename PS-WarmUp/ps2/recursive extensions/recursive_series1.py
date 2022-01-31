'''
ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern
pattern1.
product and bruteforce

pattern2.
custom product

ps2. applying computer algorithms to problem
ps2.1. utilizations

utils 1
product of itertools

utils 2
recursive
!! 쉘로우 카피 유의

ps2.2. integrations

ps3. Impl
'''
from itertools import product

import string

# control poiint of recursive fork
def promising(depth, limit, result):
    # promising or not
    promising=False
    # all implicit forks are possible, so there is no conditions of promising
    promising=True
    if(promising):
        if(depth>=limit):
            return 1
        else:
            # not fit but promising or not fit and unpromising 
            return 0

# recursive for product
def recursive(depth, limit, result):
    global samplespace,results

    # print('cur progress ',result)

    token_ctrl=promising(depth, limit, result)

    if(token_ctrl==1):
        # print(result)
        results.append(result[:])
    elif(token_ctrl==0):
        for idx_fork,val_fork in enumerate(samplespace):
            result.append(val_fork)
            recursive(depth+1, limit, result)
            result.pop()
    else:
        pass

if __name__=="__main__":
    n,r = map(int, input().split())

    global samplespace, results

    samplespace=string.ascii_lowercase[:n]
    # print(samplespace)
    results=[]

    # applying product of itertools
    # 만약 백트래킹 요건이 없이 bruteforce한 문제가 나온 경우, 요긴하다만
    # 대체로 백트래킹 조건이 1개라도 존재하면 무용지물이 되서 활용도가 낮다.
    # 그렇기에 recursive 구조의 custom product도 학습한다.
    results=list(product(samplespace,repeat=r))
    # print(results)

    depth=0
    limit=r
    result=[]
    results=[]

    recursive(depth, limit, result)
    print(results)
    for result in results: print(''.join(result))