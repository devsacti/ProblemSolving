'''
ps1. accurate comprehension
ps1.1. analysis
n*n인 체스판에 서로 공격불가하게 n개의 퀸을 배치하는 경우의 수

ps1.2. drawing pattern, exception
우선 n이 4이고, '행'만 생각해보자
1개의 행에 2개의 이상의 퀸이 배치되면 안된다. 즉 1행 = > 1개 퀸의 1대 1 대응 관계가 성립한다.

이에 따라서 자료구조를 설계하자면, 각 인덱스가 각 행에 대응하는 길이가 4인 리스트 [0,0,0,0]를 구상하고 적용할 수 있다.
그리고 체크하자면, 1행마다 퀸은 4가지의 선택지(0부터 3)가 있고, 총 4행이므로, 4^4의 경우의 수가 존재한다.

문제 단순화 관점에서, 열이 겹치는 상황을 백트래킹하고 제외해가면서, 가령, 1행의 1열에 퀸이 존재하는데 2행의 1열에 퀸을 배치하는 경우_[0,0,?,?]_,
fit한 케이스만 저장한다.

ps2. utilizing and integration of computer algorithms

ps3. Impl
'''

# def promising(i,col):
#     k=1
#     flag=True
#     while(k<i and flag):
#         if(col[i] == col[k] or abs(col[i]-col[k]) == (i-k) ):
#             flag=False
#         k +=1
#     return flag

# control point of recursive fork
def promising(depth, limit, result):
    global samplespace,results
    # print('# at ctrl',depth, limit, result)
    # ck promising
    promising=False
    # 최소한의 요구 진행
    if(depth<=1):
        promising=True
    else:
        # 마지막에 배치된 퀸이 기존 퀸들과 비교 시 일직선상에 있나 체크
        if(result[depth-1] not in result[:depth-1]):
            # 마지막에 배치된 퀸이 기존 퀸들과 대각선상에 있나 체크, 45도 대각선이란 벡터의 요소의 길이가 같은 것으로 정의가능
            flag=True
            for idx,val in enumerate(result[:depth-1]):
                # print( abs(result[depth-1]-val) == ((depth-1) - idx) )
                if(abs(result[depth-1]-val) == ((depth-1) - idx)):
                    flag=False

            if(flag):
                promising=True

    # print('at ctrl promising', promising)
    if(promising):
        if(depth>=limit):
            return 1
        else:
            return 0

# recursive for Nqueens
def recursive(depth, limit, result):
    global samplespace,results
    # print('start',depth, limit, result)

    token_ctrl=promising(depth, limit, result)
    # print('token ',token_ctrl)
    # print()
    if(token_ctrl == 1):
        # print(result)
        results.append(result[:])

    elif(token_ctrl == 0):
        for idx_fork, val_fork in enumerate(samplespace):
            result[depth]=val_fork
            recursive(depth+1,limit, result)
            result[depth]='?'
    else:
        pass

if __name__=="__main__":
    n=int(input())
    global samplespace,results
    # 0~n-1
    samplespace=[i for i in range(n)]
    # print(samplespace)
    results=[]
    
    # queen's column place per row ;  colplace_row의 k번째 idx의 val는 k번째 row의 val열에 queen이 배치된 상태라는 것이다.
    #                         1 2 3 4
    # 가령, colplace_row=['*',2,3,1,3]란 1행 2열, 2행 3열, 3행1열, 4행 3열에 퀸이 배치되었다는 것이다.
    depth=0
    limit=n
    colplace_row = ['?']*n

    recursive(depth, limit, colplace_row)
    # print(results)
    print(len(results))