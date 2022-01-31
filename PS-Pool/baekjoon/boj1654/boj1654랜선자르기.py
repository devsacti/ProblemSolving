# 랜선 자르기

# ? 왜 e를 max로 잡아야하지, 자른다고 한다면, 최소한 자기자신보다 긴 걸로는 못자르고,
# 최소길이의 랜선이 최대값이 될것같은데....
# => 길이가 제각각인 랜선이 5개이고, 길이가 동일한 요구랜선이 5개이다.
# !! 무엇보다 각각의 랜선을 10000, 1,1,1,1 이라고 가정할때, 제일길게 요구랜선5개를 만들 방법이 뭘까?
# 10000을 2000,2000,2000,2000,2000으로 짤라서 제출하는 경우이다.

# 주어진 랜선 갯수 <= 요구랜선 이라는 조건에서 나는 무의식적으로,
# 모든 랜선을 한번은 짤라야 5개에서 최소 5개 그리고 6,7 개 나온다라고 생각했는데,
# 꼭 모든 랜선을 손댈필요가 없었다!

if __name__=="__main__":
    k,n = map(int, input().split())
    
    nums=[]
    for _ in range(k):
        cand=int(input())
        nums.append(cand)
        
    s=1
    e=max(nums)
    
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