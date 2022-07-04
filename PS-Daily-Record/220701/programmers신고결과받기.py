# ps1.comprehension
##    id별 누적신고횟수 도출
    
    
# ps2.applying algorithm
##    그래프 관점, 신고한 사람끼리 인접하게 간주 가능할듯
    
# ps3.impl
from collections import defaultdict

def solution(id_list, report, k):
    
    # id별 신고자 집합 dict for id별 신고자 누적횟수 카운팅
    id_reporterset={k:set() for k in id_list}
    # 정지된 id list
    paused=[]
    
    for item in report:
        v1,v2 = item.split()

        id_reporterset[v2].add(v1)
    
    for key,val in id_reporterset.items():
        if(len(val)>=k):
            paused.append(key)
    
    # print('reported_reporter',reported_reporter)
    # print('paused',paused)

    dict_answer={k:0 for k in id_list}

    for item in paused:
        for source in id_reporterset[item]:
            dict_answer[source]+=1
    answer = list(dict_answer.values())
    # print(answer)

    return answer