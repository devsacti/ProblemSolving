def promising(depth, limit, result):
    global samplespace,results
    # print('# at ctrl',depth, limit, result)
    # ck promising
    promising=0
    # 최소한의 요구 진행
    if(depth<=1):
        promising=1
    else:
        # 마지막에 배치된 퀸이 기존 퀸들과 비교 시 일직선상에 있나 체크
        if(result[depth-1] not in result[:depth-1]):
            # 마지막에 배치된 퀸이 기존 퀸들과 대각선상에 있나 체크, 45도 대각선이란 벡터의 요소의 길이가 같은 것으로 정의가능
            diagonal_token=True
            for idx,val in enumerate(result[:depth-1]):
                # print( abs(result[depth-1]-val) == ((depth-1) - idx) )
                if(abs(result[depth-1]-val) == ((depth-1) - idx)):
                    diagonal_token=False
            if(diagonal_token):
                promising=1

    # print('at ctrl promising', promising)
    if(promising==1):
        
        if(depth < limit):
            return 1
        else:
            # depth == limit
            return 2
    else:
        #promising is 0
        return 0

# recursive for Nqueens
def recursive(depth, limit, result):
    global samplespace,results
    # print('start',depth, limit, result)

    # promising token ; 0, 1, 2 ; unpromising, promising, promising && Fit
    promising_token=promising(depth, limit, result)
    # print('cur token',promising_token)
    if(promising_token==0):
        return
    elif(promising_token==1):
        for idx_fork, idx_deploy in enumerate(samplespace):
            result[depth]=idx_deploy
            recursive(depth+1,limit, result)
            result[depth]='?'
    else:
        results.append(result[:])
        return

def solution(n):
    answer = 0
    global samplespace,results
    # 0~n-1
    depth=0
    limit=n
    #
    samplespace=[i for i in range(n)]
    results=[]
    result = ['?']*n

    recursive(depth, limit, result)
    answer=len(results)
    return answer
