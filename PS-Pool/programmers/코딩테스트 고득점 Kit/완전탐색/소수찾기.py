# ps1. comprehension
# 종이조각을 이어붙일 때, 중복불가, 순서 존재 ; permutations
# 소수판별 필요

# ps2. applying algorithms
# module 1 ; 전체 경우의 수 구하기 및 전처리 => int가 알아서 해줌
# module 2 ; 소수판별

# ps3. impl
from itertools import permutations
from math import *

def check(num):
    token_primary=False
    divs=[]
    
    # print('num ',num)

    for div in range(1, floor(sqrt(num)) + 1 ):
        rest=num%div
        quoto=num//div
        if(rest==0):
            divs.append(div)
            # correspond one of pair
            divs.append(quoto)
    # print(divs)
    
    if len(divs)==2:
        token_primary=True
    else:
        pass
    
    return token_primary
        

def solution(numbers):
    
    nums=list(numbers)
    # print(nums)
    
    allcases=[]
    
    for r in range(1, len(nums)+1):
        sub_cases=list(permutations(nums,r))
        
        for case in sub_cases:
            allcases.append(''.join(case))
            
    # print(allcases)
    
    # allcases 내 중복 제거 및 숫자화
    allcase2={}
    for case in allcases:
        num_case=int(case)
        allcase2[num_case]=1

    # print(allcase2)
    
    answer = 0

    for case in allcase2.keys():
        # 1은 소수가 아니나, 구조상 예외를 일으키므로 continue
        if case == 1:
            continue
        
        if check(case):
            answer+=1
    
    return answer