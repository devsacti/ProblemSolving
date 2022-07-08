# 3차원 배열 사용
# 
# 개요
# 딕셔너리를 활용해서 좌표별로 데크를 선언하고, 추가되는 무게가 아이템이고 그 순서가 아래위이다.
# 

import sys
from collections import deque

# summary of condition
# !!! yxW coordinates
# 1 특정 위치의 가장 위에 택배를 하나 올리는 명령
# 2 특정 위치의 가장 아래에 택배를 하나 끼워 넣는 명령
# 3 특정 위치의 가장 위 택배를 제거하는 명령
# 4 특정 위치의 가장 위 택배 무게를 출력하는 명령
# for example, 4 y x => (y, x) 위치의 가장 위 택배 무게를 출력한다.

coordinates={}

def warehouse(q):
    if(q[0] == 1 or q[0]==2):
        t,y,x,item = q

        if(t==1):
            if( (y,x) not in coordinates.keys()):
                coordinates[(y,x)]=deque()
                coordinates[(y,x)].append(item)
            else:
                coordinates[(y,x)].append(item)
        elif(t==2):
            if( (y,x) not in coordinates.keys()):
                coordinates[(y,x)]=deque()
                coordinates[(y,x)].appendleft(item)
            else:
                coordinates[(y,x)].appendleft(item)

    else:
        # 조건 상 해당 위치에 물건이 있나없나는 확인안해도됨
        t,y,x = q

        if(t==3):
            tmp=coordinates[(y,x)].pop()
            # print(tmp)
        elif(t==4):
            print(coordinates[(y,x)][-1] )

if __name__=="__main__":
    N,M,q = map(int, sys.stdin.readline().split())
    
    qs=[]
    for _ in range(q):
        qs.append(list(map(int, sys.stdin.readline().split())))
    
    for q in qs:
        # print(q)
        warehouse(q)
