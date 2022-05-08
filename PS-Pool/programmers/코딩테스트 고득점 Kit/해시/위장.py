'''
ps1. comprehension
경우의 수와 독립-종속 개념

ps2. applying computer algorithms

ps3. impl
난 다 맞출 생각이 없음
'''

from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    
    clothes.sort(key=lambda item : item[1])
    
    kind_clothes=defaultdict(list)
    
    for item in clothes:
        name, kind = item
        
        kind_clothes[kind].append(name)
        
    # print(kind_clothes)
    
    # 스파이가 어떻게 입을 지 결정 전 펼치듯이,
    # 의류의 종류를 나열
    kinds=list(kind_clothes)
    # print(kinds)
    
    # 종류에 대한 콤비네이션, 우선 실행
    # 최소 1종류는 선택하고, 전체 종류 선택
    for r in range(1,len(kinds)+1):
        cases=list(combinations(kinds,r))
        # print('종류에 대한 콤비네이션',cases)
    
        # 우선 1종이든 그 이상이든 어떤 종류의 의류를 입을 지는 선택된 상황
        for selected in cases:
            # print(selected)
            # combinations  출력값에 따른 부득이한 for문, 시간복잡도가 타협
            # sub는 독립케이스간 곱하기를 위한 기본 값
            sub=1
            for selected2 in selected:
                # print(selected2)
                candidates=kind_clothes[selected2]
                # print(candidates)
                # headgear라는 종류는 선택되었고, 그 중 1개
                sub *= len(list(combinations(candidates,1)))
                # print(sub)
            answer += sub
    
    return answer