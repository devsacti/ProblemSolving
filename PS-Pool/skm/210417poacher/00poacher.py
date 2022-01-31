# 밀렵꾼
# 오전 11:42 2021-04-22

# 개같게 그림이랑 예제 입력 첫번째 케이스랑 멧돼지 한마리만 f가 다르네
# 정상출력 되고 있었는데, 그림이랑 달라서 얼마나 또 스트레스 받은거야 아아아

import sys

# below has boar's y,x as key and d,f, w as value
global Boars

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

    return cur, d


def simulation(R,C,sec_th):
    global Boars
    # simulate boar's movement per sec, cuz this func is called per sec
    # simulate poacher 
    
    time=1
    cand_boars={}
    keysBoar=Boars.keys()

    for keyBoar in keysBoar:
        # cur boar
        r,c = keyBoar
        d,f,w = Boars[keyBoar]

        # print('cur boar ',r,c,d,f,w)

        if( d < 2):
            r, d=move(R,r,d,time,f)
        else:
            d-=2
            c, d=move(C,c,d,time,f)
            d+=2

        # print('future   ',r,c ,d)
        
        # r,c means cur boar's candidate of future place
        # if there is boar already, compare the w
        if( (r,c) not in cand_boars.keys() ):
            cand_boars[(r,c)]=(d,f,w)
        else:
            if(w>cand_boars[(r,c)][2]):
                cand_boars[(r,c)]=(d,f,w)
            else:
                # cur boar is eaten
                pass

    Boars=cand_boars
    # print(Boars)

    # Now, Let simulate Poacher
    # keysBoars=list(Boars.keys()) is same with below at py3 
    WeightPerSec=0

    # 2마리 이상의 경우, 해당 초에 해당하는 열이고
    # 동시에 Row가 제일 큰 한마리를 탐색해야함
    # print('cur time', sec_th)
    cand_keyboar = [keyBoar for keyBoar in list(Boars.keys()) if(keyBoar[1]==sec_th)]
    # print('cand', cand_keyboar)
    if(len(cand_keyboar)):
        cand_keyboar = sorted(cand_keyboar, key=lambda x : x[0])
        catchedboar= cand_keyboar[-1]
        # print('keyBoar ',catchedboar,'is catched at sec_th ', sec_th)
        WeightPerSec = Boars.pop(catchedboar)[2]

    return WeightPerSec


if __name__=="__main__":
    T=int(sys.stdin.readline().strip())

    catchedWs=[]
    for _ in range(1,T+1):
        Boars={}
        catchedW=0 # per Testcase

        R,C,M = map(int,sys.stdin.readline().split())
        # C also means t
        time = C

        for _ in range(M):
            # y,x ; INDEX OF COMPUTER
            y,x, d,f,w = map(int,sys.stdin.readline().split())

            d -=1 # to make index

            # 좌표의 중복이 없다고 한다.
            Boars[(y,x)]=(d,f,w)

        # print(Boars)

        for sec in range(time):
            sec_th=sec+1
            catchedW+=simulation(R,C, sec_th)
        # print(catchedW)
        catchedWs.append(catchedW)
        
    for num,val in enumerate(catchedWs,1):
        print('#'+str(num),val)


