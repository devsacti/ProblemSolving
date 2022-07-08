# ps1. comprehension
# 

# ps2. applying algorithms


# ps3. impl
# heapify ; 이진 트리 기반 최소 힙 구조
from heapq import *

def solution(scoville, K):
    answer = 0
    # print(scoville)
    heapify(scoville)
    # print('heapify ',scoville)
    
    cnt_try=0
    token_fit=False
    len_scoville=len(scoville)
    
    while scoville:
        if scoville[0]>=K:
            token_fit=True
            break
        else:
            if(len_scoville==1):
                # 최소값이 K보다 작은데, 길이가 1이면 더이상 섞질 못함
                # 더이상 token_fit을 바꿀 수 없다.
                break
            elif(len_scoville>=2):
                # print('s',scoville)
                min_val=heappop(scoville)
                min_val2=heappop(scoville)
                new_val=min_val+(min_val2*2)
                heappush(scoville,new_val)
                # print('e',scoville)
                cnt_try+=1
                
                len_scoville-=1

    # print(cnt_try)
    
    if(token_fit):
        answer=cnt_try
    else:
        answer=-1
    
    return answer