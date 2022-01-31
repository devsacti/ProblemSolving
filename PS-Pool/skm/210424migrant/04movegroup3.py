# 단체이동
#
# 키워드; 실시간 업데이트 구현의 어려움, 무엇을 기준으로 업데이트를 할것인가(좌표? or 사람?)

import sys

# review 8
# 딕셔너리에 대한 정의역 치역 해석은 좋은데, 
# 1 대 다의 관계에서는 이게 딱 맞지 않고 애당초 키값으로 부적합해서
# 정확한 역함수 역할의 딕셔너리 생성은 불가, 하지만 쓸모
# 그러니 아에 정의역 치역 처럼 이해하고, 정의역 갯수대로 while돌리는 걸 
# 받아들이자. review6처럼 거부감 가지지말자
# !! 게다가 사람 수로 for 돌리면 단순하다

# review 9
# 영역을 벗어나는 상황에 따라서 방향을 전환하긴 했는데,
# 이를 순간적으로만 +-1하지 객체정보를 수정하지 않아서 오차발생,
# 즉, 전환된 방향 정보가 '다시 벗어나기 전까지' 유지되야하는데, 그냥 첫번째 범위외를 만난 순간만 갱신됨

def move(num,N,M,yx,d):
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
        if(d==0 or d==2): d+=1
        else: d-=1
        HumantoDir[num]=d

        candy= cury + dy[d]
        candx= curx + dx[d]

    cury,curx = candy, candx

    return cury, curx


# 좌표 : 사람(num) list
COORDtoHumans={}
# 사람 : 좌표
HumantoCOORD={}
# num of human : direction
HumantoDir={}

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    # nums of human
    nums=[num for num in range(1,k+1)]
    for num in nums:
        # y, x NOT INDEX OF COMPUTER
        y,x,d = map(int, sys.stdin.readline().split())

        if( (y,x) not in COORDtoHumans.keys() ):
            COORDtoHumans[(y,x)]=list()
            COORDtoHumans[(y,x)].append( num )
        else:
            COORDtoHumans[(y,x)].append( num )

        # 1-1 coorrepondence
        HumantoCOORD[num]=(y,x)
        HumantoDir[num]=d

    # print('init',COORDtoHumans)
    # print('init',HumantoCOORD)
    # print('init',HumantoDir)
    
    for orderT in range(1,t+1):
        # print('cur time ',(orderT-1),'~',orderT)
        # print('coord ', COORDtoHumans)
        # print('human ', HumantoCOORD)
        # print('--')

        for num in nums:
            # print('num of human ',num)
            cury,curx = HumantoCOORD[num]
            d = HumantoDir[num]
            # print('cur and d ', cury,curx,d)
            nexty,nextx = move(num,N,M,(cury,curx),d)
            # print('next ',nexty,nextx)

            if( (nexty,nextx) not in COORDtoHumans.keys()):
                # 사람계 갱신, 해당 좌표의 사람 번호는 모두 재갱신
                for num in COORDtoHumans[(cury,curx)]:
                    HumantoCOORD[num]=(nexty,nextx)

                # 좌표계 상 이동 및 이전 삭제
                COORDtoHumans[(nexty,nextx)]=list()
                COORDtoHumans[(nexty,nextx)]+=COORDtoHumans[(cury,curx)]
                del COORDtoHumans[(cury,curx)]

            else:
                # 사람계 갱신, 해당 좌표의 사람 번호는 모두 재갱신
                for num in COORDtoHumans[(cury,curx)]:
                    HumantoCOORD[num]=(nexty,nextx)
                # 좌표계상 이동
                COORDtoHumans[(nexty,nextx)]+=COORDtoHumans[(cury,curx)]
                del COORDtoHumans[(cury,curx)]
    
    # print(HumantoCOORD)
    for val in HumantoCOORD.values():
        print(val[0],val[1])
