# input condition
# fucking yxz, not xyz coordinates

import sys

# lenAxis means N or M; y or x axis
# cur means current place of axis
def move(lenAxis, cur, d, t):
    # 위치와 방향도 같을때가 주기;
    # 처음으로 벽에 닿을때까지 이동거리 + 그 벽에서 원래자리로 이동거리 ; dist1 + dist1
    # + 다른 벽에 닿을때까지 거리 + 다시 원점 도착 이동거리 ; dist2 + dist2
    # 이때 dist1 +dist2 는 길이가 n인 일차원 리스트상으로 한정하면,
    # 리스트 상 1칸을 차지한 객체가 남은 n-1을 한번씩 방문해야하므로 n-1
    t %= (2*(lenAxis-1))

    delta=[-1,1]

    # 얼핏, while 도입 직전에 반복되는 코드 한번 연산시키면 되지 않나 했더니
    # 다시 보니까, while내에서 loop마다 cur + t*delta가 계산되야해서
    # 도입 시 한번 연산하지 않고, 조금 길지만 if마다 다시금 값 계산시키게
    # 코딩된거였음
    while( cur + t*delta[d] < 1 or cur + t*delta[d]> lenAxis):
        if(cur + t*delta[d] < 1):
            # 1 칸 이동 1초가 기본조건인데
            #  next가 위쪽 범위 외가 되는 상황이라면, 딱 y-1칸 변화한 상황, 
            t -= (cur-1) 
            cur = 1
            d=1
        elif(cur + t*delta[d] > lenAxis):
            t -= (lenAxis-cur)
            cur = lenAxis
            d=0
    # 위 while 후 벽을 1번 또는 2번 찍은 직후 위치에서 남은 시간 만큼 이동
    cur += t*delta[d]

    return cur

if __name__=="__main__":
    N,M, y,x, d,t = map(int, sys.stdin.readline().split())

    if( d < 2):
        y=move(N,y,d,t)
    else:
        d=d-2
        x=move(M,x,d,t)

    print(y,x)