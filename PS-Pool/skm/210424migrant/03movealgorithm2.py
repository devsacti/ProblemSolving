# 이동 알고리즘 2 (easy)
# tcp 1 ; 좌표의 중복을 놓침 -> 딕셔너리 val 을 리스트로 구현
# tcp 2 ; 사람번호를 고려하지 않은 좌표중복해결로 미완; key val 관계에 사람번호 추가
import sys

def move(lenAxis,cur,t,d,f):
    # print('#in move', lenAxis,cur,t,d,f)
    t *=f
    # t %= 2*(lenAxis-1)
    # 벽에 부딪히고 다시 돌아오는 패턴이 아니라서 주기가 없다

    # integration version of 'd 0~1' and 'd 2~3'
    delta=[-1,1,-1,1]

    cnt=0
    # cand가 범위 외라면 while, 아니라면 그 사용하지 않고 다음 cur definition
    cand =cur+ t*delta[d]

    if(cand<1 or cand>lenAxis):
        while(cur+ t*delta[d]<1 or cur+ t*delta[d]>lenAxis):
            # print('#cand cur d /',cur+ t*delta[d], cur, d)
            # if(cnt==10):break
            # cnt+=1

            if(cur+ t*delta[d]<1):
                t -= (cur-1)
                cur = 1
                # 벽에 닿으면 스탑이라 break
                break
                # if(d==0): d = 1
                # if(d==2): d = 3

            elif(cur+ t*delta[d]>lenAxis):
                t -= (lenAxis-cur)
                cur = lenAxis
                break
                # if(d==1): d = 0
                # if(d==3): d = 2

        # in this case, not turning back, stop
        # cur += t*delta[d]
    else:
        cur += t*delta[d]

    return cur

coordinatesHuman={}

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    humans=[]
    for num in range(1,k+1):
        # y, x Not INDEX OF COMPUTER
        y,x,d,f = map(int, sys.stdin.readline().split())

        coordinatesHuman[num]=(y,x,d,f)

    # print(coordinatesHuman)
    
    keylist=list(coordinatesHuman)
    movedCoordinates={}
    for num in keylist:
        y,x,d,f = coordinatesHuman[num]
        # print(y,x,'/',d,f)
        if(d<2):
            y=move(N,y,t,d,f)
        else:
            x=move(M,x,t,d,f)

        movedCoordinates[num]=(y,x,d,f)
        # print(movedCoordinates)
    coordinatesHuman=movedCoordinates
    
    # print(coordinatesHuman)
    for num in coordinatesHuman:
        y,x,d,f=coordinatesHuman[num]
        print(y,x)