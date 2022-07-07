from collections import defaultdict

def solution(nums):
    answer = 0
    len_nums=len(nums)
    # mon[num] is count of monster
    mon_cnt=defaultdict(int)
    
    for num in nums:
        mon_cnt[num]+=1
    
    kind_mon=list(mon_cnt)
    
    cnt_kind_mon=len(kind_mon)
    
    if cnt_kind_mon >= len_nums//2:
        answer=len_nums//2
    else:
        answer=cnt_kind_mon
    
    return answer