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
# 너무 복잡, 의도하는 바와 멀어진 느낌
# ->WRONG
# 알고보니 정의역 치역으로 접근하면 당연
# 결국은 좌표별이 아니라, 사람 기준 접근도 필요한듯함 

# review 7
# usednum을 통해서 일단 이미 사용한 사람은 거르긴 했지만,
# 만약 걸러진 케이스에서 좌표가 말소되면
#  그 뒤 사용은 안되서 호출됬지만 좌표가 말소된 케이스에서 에러가 뜬다.
# 가령, 1번과 2번이 동시에 (1,2)에 있고, 1번에 의해 다같이 2,2로 가서
# 1,1이 사라졌는데 2번에서 이동 후 또 1,1을 지울려고 해서 에러
# 단순히 deletedCoordinate 변수를 만들어도 어쨌거나 2,2를 기억해서 옮겨야하니
# 다소 어려워보임
# 결국 review 6 대로 사람기준 딕셔너리도 있어야하고, 생각해보면
# 딕셔너리가 정의역 치역의 관계라면, 치역 정의역 관계를 선언하는거니
# 아주 자연스럽다. 마냥 임의의 변수가 늘어나는 게 아니니 거부감 X

# review 8
# 딕셔너리에 대한 정의역 치역 해석은 좋은데, 
# 1 대 다의 관계에서는 이게 딱 맞지 않고 애당초 키값으로 부적합해서
# 정확한 역함수 역할의 딕셔너리 생성은 불가, 하지만 쓸모
# 그러니 아에 정의역 치역 처럼 이해하고, 정의역 갯수대로 while돌리는 걸 
# 받아들이자. review6처럼 거부감 가지지말자

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


# 좌표 : 사람(혹은 오브젝트 방향정보도 있어서)
COORDtoHuman={}
# 사람 : 좌표
HummantoCOORD={}

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    nums=[num for num in range(1,k+1)]
    for num in nums:
        # y, x NOT INDEX OF COMPUTER
        y,x,d = map(int, sys.stdin.readline().split())

        if( (y,x) not in COORDtoHuman.keys() ):
            COORDtoHuman[(y,x)]=list()
            COORDtoHuman[(y,x)].append( (num,d) )
        else:
            COORDtoHuman[(y,x)].append( (num,d) )

        # 1-1 coorrepondence
        HummantoCOORD[num]=(y,x)

    print('init',COORDtoHuman)
    print('init',HummantoCOORD)
    
    for orderT in range(1,t+1):
        keylist=list(COORDtoHuman)
        print('cur time and distribution ',(orderT-1),'~',orderT,keylist)
        
        # below act per 'SEC'
        for yx in keylist:
            humans = COORDtoHuman[yx]
            
            # find last human who is captain, who is the first person of that coordinate
            # who is the idx 0 of list of coordinate
            # WRONG!! THERE is only TEMP captain...all human decide one time
            for human in humans:
                num, d = human
                print('TEMP captain num ', num, 'cur and  direction',yx,d)
                # move search the valid next and decide the y,x
                y,x = move(N,M,yx,d)
                print('next by the TEMP captain ', y,x)

                # by captain's decision,
                # if there is already human, i should be integrated, and next be updated at moved
                print('#',usednums)
                if(num not in usednums):
                    if( (y,x) not in keylist ):
                        COORDtoHuman[(y,x)]=humans
                        # del ex yx
                        del COORDtoHuman[yx]
                        
                    else:
                        # integration with basic list and moved list, and update at new dict
                        COORDtoHuman[(y,x)]=COORDtoHuman[(y,x)]+humans
                        # del ex yx
                        del COORDtoHuman[yx]
                    
                    usednums.append(num)
                    print('-------after move or integration ',COORDtoHuman)
                else:
                    pass
    
    print(COORDtoHuman)
