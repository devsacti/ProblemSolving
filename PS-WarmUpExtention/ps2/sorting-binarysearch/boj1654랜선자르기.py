'''
reference : https://www.acmicpc.net/problem/1654

ps1. comprehension for problem
ps1.1. analysis

K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.
=> binary search

ps1.2. drawing pattern, exceptions

pattern1. 주어진 랜선 들 중 가장 작은 길이를 end로 설정해서 이진탐색 
=> !! exceptions
주어진 랜선 갯수 <= 요구랜선 이라는 조건에서 나는 무의식적으로,
모든 랜선을 한번은 짤라야 5개에서 최소 5개 그리고 6,7 개 나온다라고 생각했는데,
그러나 모든 랜선을 손댈필요가 없었다!

가령,
길이가 제각각인 랜선이 5개_10000, 1,1,1,1_이고, 길이가 동일한 요구랜선이 5개이라고 할때,
제일길게 요구랜선5개를 만들 방법이 뭘까?
10000을 2000,2000,2000,2000,2000으로 짤라서 제출하는 경우이다.
즉, 1에는 손을 안대도 된다.

ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing computer algorithms

module 1 ; binary search
start is 1, end is max length of given lan lines

ps2.2. integration

ps3. Impl
'''

def bs(start,end,nums):
    # module 1 ; binary search
    s=start
    e=end
    
    while(s<=e):
        mid=(s+e)//2
        
        total_cnt=0        
        for num in nums:
            total_cnt+=(num//mid)
            
        if(total_cnt>=n):
            max_len=mid
            s=mid+1
        else:
            e=mid-1
            
    print(e)
    print(max_len)

if __name__=="__main__":
    k,n = map(int, input().split())
    
    nums=[]
    for _ in range(k):
        cand=int(input())
        nums.append(cand)
    s=1
    e=max(nums)
    
    bs(s,e,nums)