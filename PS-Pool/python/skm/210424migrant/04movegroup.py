# 단체이동
#
# 키워드; 실시간 업데이트 구현의 어려움

import sys

# tcp 1
# 매 초마다 1번 사람부터 k 번 사람까지 순서대로 이동하며,
# 각 사람이 이동할 때 같은 위치에 있는 다른 사람들도 함께 이동한다.
# => dog sound, i think but it means that i should think the move 'per sec'
# cuz the move of object is not seperate, when they meet each other, i should make them 1 set

# review 2
# 좌표이동에 특화된 massivemove 형태를 유지하면서 bfs를 하면 코드가 너무 길어진다. 
# 하지만 지금은 연습할 시간인데, 현재 문제자체가 '이동'만 고려할게 아니라
# 이동 후 좌표의 상태를 살펴야한다. 처음에는 move에 다 넣을까했는데
# 그러면 복잡해지니 별도의 함수 추가

# review 3
# 연습에 의미를 두고, 한축한축 접근,계산하는 massivemove꼴이 적용은 가능은한데
# 어짜피 2차원상의 의미로 환원되서 주변의 의미를 탐색해야하는 현재에 '부적절한'접근이라는 판단
# 일단 큰틀은 basic bfs에 만약 t,f가 크고, 특별히 이동과정에 의미가 없다면,
# 한 축식 접근하는 massivemove를 sub module로 가질 수 있다고 기록만하고 다시 회귀


# review 4 좌표기준 딕셔너리, 사람번호 딕셔너리 둘 다 선언?
# cpp이라면 그냥 되는대로 개별 매트릭스 선언해두면 될것같은데, 파이썬의 왠지모를 느림 고려 시
# 전자는 전자만으로 되지만 후자의 경우 다소 불편하니 전자로 결정

# review 5 accuracy
# 각 사람이 이동할 때 같은 위치에 있는 다른 사람들도 함께 이동한다.
# => 나는 이때 이동방향을 captain이 결정한다고 생각했는데, 나의 왠지모를 왜곡
# 물론 집단의 방향은 1개인데, 2명이 들어가있으니, 선별이 필요하다고 나도 모르게 비약
# 힘내자

# review 6
# 사람이 한명 이동할때마다, 중복발생 시 다시 keylist를 재정의하는 방식을 고안했고 될것같지만
# 너무 복잡, 의도하는 바와 멀어진 느낌,
# 결국은 좌표별이 아니라, 사람 기준 접근도 필요한듯함

def _massivemove(lenAxis,cur,t,d,f):
    # print('#in move', lenAxis,cur,t,d,f)
    # t *=f
    # t %= 2*(lenAxis-1)
    # # 벽에 부딪히고 다시 돌아오는 패턴이 아니라서 주기가 없다

    # integration version of 'd 0~1' and 'd 2~3'
    delta=[-1,1,-1,1]

    while(t):
        cand =cur+ t*delta[d]
        
        if(cand <1 or cand>lenAxis):
            #dont move, first change dir and next move
            if(cand<1):
                if(d==0): d=1
                elif(d==2): d=3

                cand =cur+ t*delta[d]
            elif(cand>lenAxis):
                if(d==1): d=0
                elif(d==3): d=2

                cand =cur+ t*delta[d]
        # 일단, 범위외만 아니면 다음칸으로 이동
        cur = cand
        t-=1

    return cur

def move(N,M,yx,d):
    cury, curx = yx

    # direction vector, m is magnitude
    m = 1
    dy=[-m,m,0,0]
    dx=[0,0,-m,m]
    kinds_dir=len(dy)

    # one dir 
    candy= cury + dy[d]
    candx= curx + dx[d]

    if(candy<1 or candy>N or candx<1 or candx>M):
        d+=1
        candy= cury + dy[d]
        candx= curx + dx[d]

    cury,curx = candy, candx

    return cury, curx


# 좌표를 중심으로 한 
coordinatesHuman={}

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    humans=[]
    for num in range(1,k+1):
        # y, x Not INDEX OF COMPUTER
        y,x,d = map(int, sys.stdin.readline().split())

        if( (y,x) not in coordinatesHuman.keys() ):
            coordinatesHuman[(y,x)]=list()
            coordinatesHuman[(y,x)].append( (num,d) )
        else:
            coordinatesHuman[(y,x)].append( (num,d) )

    print('init',coordinatesHuman)
    
    for orderT in range(1,t+1):
        keylist=list(coordinatesHuman)
        tokens=len(keylist)
        print('cur time and distribution ',(orderT-1),'~',orderT,keylist)

        # !!! if there is already, break to redefinition of keylist after dup
        # if not, update at moved
        while(tokens):
            overloaded_keylist=keylist=list(coordinatesHuman)
            # below act per 'SEC'
            for yx in keylist:
                humans_coordinates = coordinatesHuman[yx]
                # find last human who is captain, who is the first person of that coordinate
                # who is the idx 0 of list of coordinate
                # WRONG!! THERE is only TEMP captain...all human decide one time
                for human in humans_coordinates:
                    num, d = human
                    print('TEMP captain num ', num, 'cur and  direction',yx,d)
                    # move search the valid next and decide the y,x
                    y,x = move(N,M,yx,d)
                    print('next by the TEMP captain ', y,x)
    
                    # by captain's decision, which token is not used, list is moved or integrated,
                    # if not, update directly at moved
                    # if there is already human, i should be integrated, and next be updated at moved
                    if( (y,x) not in coordinatesHuman.keys() ):
                        coordinatesHuman[(y,x)]=list_human
                        # del ex yx
                        del coordinatesHuman[yx]
                        
                    else:
                        # integration with basic list and moved list, and update at new dict
                        coordinatesHuman[(y,x)]=coordinatesHuman[(y,x)]+list_human
                        # del ex yx
                        del coordinatesHuman[yx]
                        break

                    print('-------after move or integration ',coordinatesHuman)

            tokens-=1

    
    print(coordinatesHuman)
    # for num in coordinatesHuman:
    #     y,x,d,f=coordinatesHuman[num]
    #     print(y,x)