# ps1. accurate comprehension
# ps1.1. analysis
# n*n인 체스판에 서로 공격불가하게 n개의 퀸을 배치하는 경우의 수

# ps1.2. drawing pattern, exception
# 우선 n이 4이고, '행'만 생각해보자
# 1개의 행에 2개의 이상의 퀸이 배치되면 안된다. 즉 4개의 퀸은 우선 행마다 1개씩 배치되야한다
# 여기까지만 생각하면 1행마다 퀸은 4가지의 선택지가 있고, 총 4행이므로, 4^4의 경우의 수가 존재한다.

# 문제 단순화 관점에서, 열이 겹치는 상황을 제쳐두고,
# 이제는 브루트 포스하게 퀸을 배치해보되, 다른 퀸의 공격영역에 들어간 경우 백트래킹을 한다.

# ps2. utilizing and integration of computer algorithms

# ps3. Impl

def promising(i,col):
    k=1
    flag=True

    while(k<i and flag):
        if(col[i] == col[k] or abs(col[i]-col[k]) == (i-k) ):
            flag=False
        k +=1
    return flag

def n_queens(i,col):
    global cnt_validcase
    n=len(col) - 1

    if(promising(i,col)):
        if(i==n):
            print(col[1:n+1])
            cnt_validcase+=1
        else:
            for j in range(1, n+1):
                col[i+1] =j
                n_queens(i+1,col)

if __name__=="__main__":
    n=int(input())
    global cnt_validcase
    cnt_validcase=0

    col = ['*']+[0]*n

    n_queens(0,col)

    print(cnt_validcase)