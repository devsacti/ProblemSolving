# ps1. comprehension
# 디스크는 당장 그것이 무엇인지는 모르지만, 적합한 우선순위 기준에 따라
# 우선순위에 따라 작업을 수행할 때 최소 작업 시간에 접근한다.

# 적합한 우선순위 기준은 무엇인가?
# 현재 디스크가 비어있다면, 어떤 일이든 우선 시작
# 2개이상 대기중이면, 작업소요시간이 작은 것부터한다
# 디스크는 우선순위에 따라 작동해야한다

## 우선 따라쳤으나, 반복 필요

# ps2. applying algorithms
# 우선순위 큐로 디스크를 묘사
# 일 시작 전에 디스크를 재정렬

# ps3. impl

# ps4. references
# https://soohyun6879.tistory.com/136

from heapq import *
from math import *

from collections import deque

def solution(jobs):
    answer = 0
    # 처리해야할 작업 수, 처리완료한 작업 수 ; 이 변수 비교를 통해 모든 작업이 수행된지 체크
    cnt_jobs=len(jobs)
    # 
    cnt_complete=0
    
    # 시간축에 대응하는 x축은 0 부터 시작이고, 처리의 편리함을 위해 -1로 정의
    point_pre_now = -1
    # 시간 축에서 변화하는 현재 시각에 대응하는 변수
    point_now = 0
    
    # 디스크 대기 우선 순위 큐
    wait_heap=[]
    
    while cnt_complete<cnt_jobs:
        # 우선 '현재 시점에서' 처리해야할 모든 남은 작업들을 펼치는 것
        # 디스크 대기 큐에 넣는다 ; 디스크 대기 큐이지 디스크는 아니므로 모두 넣는다.
        # 디스크에 들어갈 대기 큐 0번째만이 전달되고 처리되었다고 간주하고 pop될 예정이다.
        for job in jobs:
            # print(job)
            # 우선은 도착 시간을 기준으로, 그리고 유효한 job을 대기 큐에 넣는다.
            if point_pre_now < job[0] <= point_now:
                heappush(wait_heap, [ job[1],job[0] ] )
        
        # print('wait_heap',wait_heap)
        
        if len(wait_heap) > 0:
            cur = heappop(wait_heap)
            # print('cur',cur)
            # 대기 힙 큐의 첫번째가 pop된 순간, 작업은 시작되었고
            # 종료 시각은 현재 시각 + 작업의 소요시간이 된다.
            # 그 전에 앞서서, while의 다음 시행에서 도착시간을 기준으로 유효job을 넣기 위해 prev_now갱신
            point_pre_now = point_now
            point_now = point_now + cur[0]
            
            answer += point_now - cur[1]
            cnt_complete+= 1
        else:
            # 중간에 아직 도착하지 않는 작업을 대기하는 경우, 1ms 씩 증가
            point_now += 1
    
    return answer // cnt_jobs