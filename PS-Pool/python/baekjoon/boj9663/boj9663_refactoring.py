# not complete yet

# ps1. accurate comprehension
# ps1.1. analysis
# n*n인 체스판에 서로 공격불가하게 n개의 퀸을 배치하는 경우의 수

# ps1.2. drawing pattern, exception
# 우선 n이 4이고, '열'만 생각해보자
# 1개의 열에 2개의 이상의 퀸이 배치되면 안된다. 즉 4개의 퀸은 우선 열마다 1개씩 배치되야한다
# 여기까지만 생각하면 1열마다 퀸은 4가지의 선택지가 있고, 총 4열이므로, 4^4의 경우의 수가 존재한다.

# 문제 단순화 관점에서, 행이 겹치는 상황을 제쳐두고,
# 이제는 브루트 포스하게 퀸을 배치해보되, 다른 퀸의 공격영역에 들어간 경우 백트래킹을 한다.

# ps2. utilizing and integration of computer algorithms

# ps3. Impl

# 퀸 놓아보기 함수 
def n_queens(i, row) : 
    global result # 글로벌로 생성
    n=len(row)

    print(row)
    # 재귀 빠져나가기 
    if(i == n):
        print(row[0:n]) 
        result+=1 
    # 재귀 빠져나갈 수 없을 때 퀸을 놓아보고 이전 퀸들과 비교. 
    else : 
        for j in range(n) : 
            row[i] = j # for문이 break 걸리지 않고 다 돌면 else(재귀) 실행 
            for k in range(i):
                # 한 열에 하나씩 들어가므로 열 바교는 필요없다. 또한 대각선은 수학식을 생각해보면 쉽게 구할 수 있다. 
                if(row[k] == row[i] or abs(row[k]-row[i]) == (i-k) ): 
                    break 
                else : 
                    n_queens(i+1, n) 

if __name__=="__main__":
    n = int(input())

    global result
    result = 0 
    
    row = [None]*n

    n_queens(0, row) 

    print(result)
