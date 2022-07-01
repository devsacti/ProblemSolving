# 이 코드의 핵심은 ps3

# ps3.
# promising 보다 depth를 우선해서 배치할 시의 자료구조상 result에 1칸을 더 추가해야하고
# 근사할뿐 모든 케이스에서 정답이 나오지 않음

def is_promising(depth, result):
    token_ctrl=None
    # 우선 0번째, 1번째 열까지는 배치하여 depth는 그 다음인 상태에서 상황판단
    if(depth<=1):
        token_ctrl=1
    else:
        # 우선 마지막에 배치된 퀸이 기존 퀸들과 비교 시 일직선상에 있나 체크
        if(result[depth-1] not in result[:depth-1]):
            # print('#',result)
            # 마지막에 배치된 퀸이 기존 퀸들과 대각선상에 있나 체크, 45도 대각선이란 벡터의 요소의 길이가 같은 것으로 정의가능
            for idx_col,idx_deploy in enumerate(result[:depth-1]):
                # print( abs(result[depth-1]-val) == ((depth-1) - idx) )
                if( abs(result[depth-1]-idx_deploy) == ( (depth-1) - idx_col) ):
                    token_ctrl=0
                else:
                    token_ctrl=1
                    # print('##',result)
    
    return token_ctrl

# recursive for Nqueens
def recursive(depth, limit, result):
    if depth>limit:
        results.append(result)
        return
    else:
        token_ctrl=is_promising(depth, result)
    
        if(token_ctrl == 1):
            for idx_deploy in range(limit):
                result[depth]=idx_deploy
                recursive(depth+1,limit, result)
                result[depth]=-1
            
        elif(token_ctrl == 0):
            return
        else:
            pass

def solution(n):
    global record
    global results
    answer = 0
    
    #
    depth=0
    limit=n
    result=[-1 for _ in range(n+1)]
    results=[]
    #
    recursive(depth, limit, result)
    answer= len(results)//n
    return answer