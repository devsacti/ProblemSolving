'''
ps1.comprehension
    id별 누적신고횟수 도출
    
    
ps2.applying algorithm
    그래프 관점, 신고한 사람끼리 인접하게 간주 가능할듯
    
ps2.impl

# update error ; 최종 집계 후 paused 산출하지 않으면,
len(?) == k 방식이더라도

중복 신고로, 여전히 set에 새로운 이름이 안들어갔지만,
이거는 이거대로 len(?) 시 값이 유지되고,

if문에 또 집계되서 paused에 가령 muzi가 2번 들어감

한마디로 최종집계와 판단을 독립시키는 구현이 필요함
'''
from collections import defaultdict

def solution(id_list, report, k):
    
    # 누적 신고횟수 dict
    reported_reporter={k:set() for k in id_list}
    # 정지된 id list
    paused=[]
    
    for item in report:
        v1,v2 = item.split()

        reported_reporter[v2].add(v1)
    
    for key,val in reported_reporter.items():
        if(len(val)>=k):
            paused.append(key)
    
    # print('reported_reporter',reported_reporter)
    # print('paused',paused)

    dict_answer={k:0 for k in id_list}

    for item in paused:
        for source in reported_reporter[item]:
            dict_answer[source]+=1
    answer = list(dict_answer.values())
    # print(answer)

    return answer