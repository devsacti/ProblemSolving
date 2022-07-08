# N명 이동
import sys

global N,M,k,t

# lenAxis means N or M; y or x axis
# cur means current place of axis
def move(lenAxis, cur, d, t, f):
    # f칸 이동에 1초인 것을 기존 발견한 t 주기를 활용하기 위해
    # 시간을 치환해서_1칸 f초_1칸 이동 1초 시 t 주기 활용
    t =t*f
    t %= (2*(lenAxis-1))

    delta=[-1,1]

    while( cur + t*delta[d] < 1 or cur + t*delta[d]> lenAxis):
        if(cur + t*delta[d] < 1):
            # next가 위쪽 범위 외가 되는 상황이라면, 딱 y-1칸 변화한 상황, 
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
    N,M,k,t = map(int, sys.stdin.readline().split())

    # k is correspods with cnt of human
    humans=[]
    for _ in range(k):
        human= map(int, sys.stdin.readline().split())
        humans.append(human)

    for human in humans:
        # r, c;  NOT INDEX OF COMPUTER
        r,c, d,f = human

        if( d < 2):
            r=move(N,r,d,t,f)
        else:
            d=d-2
            c=move(M,c,d,t,f)

        print(r,c)
