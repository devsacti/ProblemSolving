#역방향 밀기

import sys
from collections import deque

if __name__=="__main__":
    n,k=map(int,sys.stdin.readline().split())
    nums=sys.stdin.readline().split()
    dq_nums=deque(nums)

    for _ in range(k):
        dq_nums.append(dq_nums.popleft())
    
    nums=list(dq_nums)
    print(' '.join(nums))