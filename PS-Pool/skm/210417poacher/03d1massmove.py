import sys

if __name__=="__main__":
    # n means length of list
    # x means cur place
    # d means direction
    # t means time to execute
    n,x, d,t = map(int, sys.stdin.readline().split())

    # 방향이 있기때문에 단순히 맨처음으로 처음 자리로 간다고 주기가 아니라
    # 방향도 같을때가 주기
    # t=t%(2*n-2)
    t %= (2*n-2)

    # matrix=[0 for _ in range(n)]
    # matrix[idx_x]=1
    # print(matrix)

    dx=[-1,1]

    # 1개 1개 빼고 더하고 있으면 시간초과
    # for _ in range(t):
    #     # matrix[idx_x]=0
    
    #     cand_x=idx_x+dx[d]
    #     if(cand_x==-1 or cand_x==n):
    #         if(d==0): d=1
    #         else: d=0
    #         cand_x=idx_x+dx[d]
        
    #     idx_x=cand_x
    #     # matrix[idx_x]=1
    #     # print(matrix)

    # 한번에 끝까지 이동하고 x를 이용해서 여분의 times를 업데이트;
    #  1씩 7번 이동 -> x를 통해서 4한번에 쓰고, 3남겨주고 방향전환
    while( x + t*dx[d] < 1 or x + t*dx[d]>n):
        if(x + t*dx[d] < 1):
            t-= (x-1)
            x=1
            d=1
        elif(x + t*dx[d] < n):
            t-= n-x
            x=n
            d=0

    x += t*dx[d]

    print(x,d)
