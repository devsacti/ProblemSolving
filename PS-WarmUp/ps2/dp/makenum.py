# summary

# ps
## step1

## step2

## step3 ; implementation

def makeDPtable(n):
    # init DP table
    # N-1에서 1을 더해, N되는 경우 생각 길이는 N
    # 1 base indexing
    DPtable=['*']+[0]*n
    
    # 1,2,3으로
    # 1을 만드는 경우 1개, 2를 만드는 경우 2개, 3을 만드는 경우 4개
    DPtable[1]=1
    DPtable[2]=2
    DPtable[3]=4
    
    # 4이상에 대해 작동
    for i in range(4,n+1):
        # if i가 4면 
        # dptable[1]에 3을 더하는 경우,
        # dptable[2]에 2을 더하는 경우,
        # dptable[3]에 1을 더하는 경우,
        # 들의 합
        DPtable[i]=(DPtable[i-3]+DPtable[i-2]+DPtable[i-1])%1000007
        
    print(DPtable[n])

if __name__=="__main__":
    n=int(input())
    
    # 1d DP table for recording kinds of making num
    makeDPtable(n)