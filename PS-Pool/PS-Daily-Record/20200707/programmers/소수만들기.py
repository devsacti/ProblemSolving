from itertools import combinations
from math import *

def check_primary(num):
    limit=int(sqrt(num))
    
    pre_divisors=[]
    post_divisors=[]
    for divisor in range(1,limit+1):
        if num%divisor==0:
            pre_divisors.append(divisor)
            post_divisors.append(num//divisor)
    pre_divisors.extend(list(reversed(post_divisors)))
    divisors = pre_divisors[:]
    if len(divisors)==2:
        return True
    else:
        return False

def solution(nums):
    answer = 0
    
    for case in list(combinations(nums,3)):
        # print(case)
        num=sum(case) # v
        # print(num)
        if check_primary(num):
            answer+=1
            
    return answer