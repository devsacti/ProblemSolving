'''
ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern
pattern1.
combinations and bruteforce

pattern2.
custom combinations

문자 그대로 permutaions의 조건에 '순서를 고려하지 않는 것'이 추가되는 것에 집중한다면,
개별 result들을 정렬을 통해 순서를 통일 후하여 오름 차순에서 비교한 뒤 없을 때 results에 저장할 수 있다.

혹은, 말그대로 기존에 사용한 조합인지 아닌지를 판단할 변수_choosed_를 활용하여 개별 result가 이미 사용된 조합인지 체크한다.
아무쪼록 이러한 패턴들은 시간복잡도가 매우 커 보인다.

ps2. applying computer algorithms to problem
ps2.1. utilizations

utils 1
combinations of itertools

utils 2
recursive

ps2.2. integrations

ps3. Impl
'''
from itertools import combinations

import string

# control poiint of recursive fork
def promising(depth, limit, result):
    global results
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
            
            if(limit== (0 or 1)):
                return 1
            
            if(result[depth-1] != result[depth-2]):
                # 기존 permutations 에 정렬을 통해 순서를 무마하고, results에 이미 존재하는지 체크한다.
                # 그리고 여기에선 쉘로우 카피를 활용하여 정렬된 result를 리턴하는 과정을 생략한다.
                result=sorted(result)
                # print('# ck',result)
                if result not in results:
                    return 1
                else:
                    return -1
        else:
            return 0

# recursive for combinations
def recursive(depth, limit, result):
    global samplespace,results

    print('cur progress ',result)

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

    # applying combinations of itertools
    # 만약 백트래킹 요건이 없이 bruteforce한 문제가 나온 경우, 요긴하다만
    # 대체로 백트래킹 조건이 1개라도 존재하면 무용지물이 되서 활용도가 낮다.
    # 그렇기에 recursive 구조의 custom combinations 학습한다.
    results=list(combinations(samplespace,r))
    # print(results)

    depth=0
    limit=r
    result=[]

    # 개별 결과를 정렬하는 방식으로 순서를 무마한 뒤, results에 값이 존재하나 안하나 체크하여 중복조합을 제거한다.
    results=[]

    recursive(depth, limit, result)
    print(results)

    for result in results:print(''.join(result))