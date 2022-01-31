# 단순 밀기
# 오전 10:18 2021-04-24

import sys

if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))

    # insert(index,item)
    nums.insert(0,0)
    tmp=nums.pop()

    for num in nums:
        print(num, end=' ')