# 이동 알고리즘 3 ; from 단체 이동, 이동알고리즘 2(easy)
#
# 키워드; 실시간 업데이트 구현의 어려움, 무엇을 기준으로 업데이트를 할것인가(좌표? or 사람?)

import sys

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
        BoxtoDir[num]=d

        candy= cury + dy[d]
        candx= curx + dx[d]

    cury,curx = candy, candx

    return cury, curx


# 좌표 : 박스(num) list
COORDtoBoxes={}
# 박스 : 좌표
BoxtoCOORD={}
# num of human : direction
BoxtoDir={}

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    # nums of human
    nums=[num for num in range(1,k+1)]
    for num in nums:
        # y, x NOT INDEX OF COMPUTER
        y,x,d = map(int, sys.stdin.readline().split())

        if( (y,x) not in COORDtoBoxes.keys() ):
            COORDtoBoxes[(y,x)]=list()

        COORDtoBoxes[(y,x)].append( num )

        # 1-1 coorrepondence
        BoxtoCOORD[num]=(y,x)
        BoxtoDir[num]=d

    # print('init',COORDtoBoxes)
    # print('init',BoxtoCOORD)
    # print('init',BoxtoDir)
    
    for orderT in range(1,t+1):
        # print('cur time ',(orderT-1),'~',orderT)
        # print('coord ', COORDtoBoxes)
        # print('human ', BoxtoCOORD)
        # print('--')

        for num in nums:
            # print('num of Box ',num)
            cury,curx = BoxtoCOORD[num]
            d = BoxtoDir[num]
            # print('cur and d ', cury,curx,d)
            nexty,nextx = move(num,N,M,(cury,curx),d)
            # print('next ',nexty,nextx)

            # slicing the parts; left or unit of gone
            cand=COORDtoBoxes[(cury,curx)]
            std=cand.index(num)
            # print(cand,std)
            if(std==0): left=list()
            else:  left=cand[:std]
            unit=cand[std:]
            
            # 박스 기준 갱신, 현재 넘버 뒤쪽으로만 이동
            for num in unit:
                BoxtoCOORD[num]=(nexty,nextx)
            # 좌표 기준 갱신,
            if( (nexty,nextx) not in COORDtoBoxes.keys()):
                COORDtoBoxes[(nexty,nextx)]=list()

            COORDtoBoxes[(nexty,nextx)]+=unit
            COORDtoBoxes[(cury,curx)]=left

    
    # print(BoxtoCOORD)
    for val in BoxtoCOORD.values():
        print(val[0],val[1])
