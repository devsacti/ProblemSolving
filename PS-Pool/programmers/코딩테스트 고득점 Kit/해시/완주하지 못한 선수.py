'''
ps1. comprehension

    우선 hash 관련 dict 활용
    
    동명이인 예외처리


ps2. applying algorithms

ps3. impl

한편, 정렬된 상태라면?, 미완주자가 처음, 중간, 끝에 있는 경우들 커버

'''
from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    dict_parti=defaultdict(list)
    
    for parti in participant:
        dict_parti[parti].append(parti)
    
    # print(dict_parti)
    
    for comp in completion:
        dict_parti[comp].pop()
        
        if(len(dict_parti[comp])==0):
            del dict_parti[comp]
    
    # print(dict_parti.keys())
    li_answer=list(dict_parti.keys())
    answer=li_answer[0]
    
    return answer