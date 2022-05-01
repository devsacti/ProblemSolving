'''
ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern
pattern1.
permutations and bruteforce

pattern2.
custom permutations

ps2. applying computer algorithms to problem
ps2.1. utilizations

utils 1
permutations of itertools

utils 2
recursive

ps2.2. integrations

ps3. Impl
'''
from itertools import permutations

import string

# control poiint of recursive fork
def promising(depth, limit, result):
    # print(depth,limit,result, end='=>')

    # promising or not
    promising=False
    if(len(result)>=2):
        # print('ck ',result[:depth-1],end=' ')
        if(result[-1] not in result[:depth-1]):
            promising=True
    else:
        promising=True


    # if it is promsing,then fit or not
    # print('promising', promising)
    if(promising):
        # fit or not
        if(depth>=limit):

            if(limit== 0 or 1):
                return 1

            if(result[depth-1] != result[depth-2]):
                return 1
            else:
                return -1
        else:
            return 0

# recursive for permutations
def recursive(depth, limit, result):
    global samplespace,results

    # print('cur progress ',result)

    token_ctrl=promising(depth, limit, result)

    if(token_ctrl==1):
        # print('when token_ctrl is 1, result',result)
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

    # applying permutations of itertools
    # 만약 백트래킹 요건이 없이 bruteforce한 문제가 나온 경우, 요긴하다만
    # 대체로 백트래킹 조건이 1개라도 존재하면 무용지물이 되서 활용도가 낮다.
    # 그렇기에 recursive 구조의 custom permutaions도 학습한다.
    results=list(permutations(samplespace,r))
    print(results)

    depth=0
    limit=r
    result=[]
    results=[]

    recursive(depth, limit, result)
    # print(results)

    for result in results:print(''.join(result))