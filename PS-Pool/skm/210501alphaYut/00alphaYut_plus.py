# 알파윷
# 오전 1:12 2021-05-02
# summary
# core; itertools.product and move algorithm

# lesson 3 ; greedy vs bruteforce
# 근사값과 정확한 답 ; 2035 vs 2050
# !!!!!!!! 하위모듈 문제랑 주어진 문제가 다르더라...!!!
# 하위모듈 문제와 달리, 또한, 제외된 말에 이동 명령을 내릴 수 없다. 라는 구문이 추가됨...

# lesson 4 ; 할당을 최소화해서 또 시간소요를 최소화 해보자
# 일단 딕셔너리 다 쪼개서 리스트로 만들고

import sys
from itertools import product

# description of datastructer about given situdation
# part 0~2
path0=[0,5,10,15,20,50,30,35,40,45,100,55,60,65,70,75,80,85,90,95,500,1000]
path10=[50,275,250,300,150,175,75,80,85,90,95,500,1000]
path11=[300,350,400,500,1000]
path2=[100,150,125,300,350,400,500,1000]

path={ 
    0 : path0,
    1 : path10, 11 : path11,
    2 : path2
}

# summmary of variables
# A,B,C,D pieces => 1,2,3,4
pieces = [ i for i in range(1,5)]

# dict를 자연스럽게 2차원 테이블이라고 생각하면 pathCode, cumDist가 사실상 row와 column 역할
# piece_place ; dict , piece to place(pathCode&cumDist) 
piece_place = { piece : (0,0) for piece in pieces}
# piece_Points ; dict , piece : Point 
piece_Points ={ piece : 0 for piece in pieces}

def checkjunction(pathCode,cumDist):
    # 분기점 이후 경로들, part 1~2
    tokenChange=False
    # 유지 시 입력된 default가 리턴됨

    if(pathCode==0 and cumDist==5):
        tokenChange=True
        pathCode=1
    elif(pathCode==0 and cumDist==10):
        tokenChange=True
        pathCode=2
    # sub of part 1
    if(pathCode==1 and cumDist==3):
        tokenChange=True
        pathCode=11

    # 분기점도착에 따라, 새로운 pathCode를 할당 받는 경우, cumDist초기화
    if(tokenChange): cumDist=0
    # print('next changing path ?', tokenChange)
    return pathCode,cumDist,tokenChange

# 장기말(piece) 별로, 이동해야할 칸수를 입력받아 결과를 장기말별 딕셔너리에 저장
def simulation(piece, MD):
    token_duplication=False

    pathCode, cumDist = piece_place[piece]
    preserved=(pathCode,cumDist) # for duplication of piece
    Point = piece_Points[piece]
    # print(piece, 'piece', pathCode,',',cumDist, end=' ')
    # print('HavingPoint',Point)
    # print('1d vector ', MD)

    # step1 ; 현재 경로 상 누적 이동거리에 따른 방문 및 점수 획득
    curPath=path[pathCode]
    cumDist+=MD
    # step1.5 ; 현재 경로 리스트의 맨끝 인덱스에 도달 = 목표점 도달, 종료
    if(cumDist>=len(curPath)-1):
        Point=curPath[-1]

        #update the place to distinguish, point
        piece_place[piece] = (-1,-1)
        piece_Points[piece] = Point
        # print(piece, 'piece', piece_place)
        # print(piece, 'piece', piece_Points)
    else:
        # step2 ; 현재 경로 상 위치에서 경로 유지 또는 변경 파악 => 최신화가 우선되야, 후속 겹침유무 판단가능
        # 구분 1 ;  pathcode의 변경(tokenChange 연동) => 변경시 cumDist 는 0 아니면 누적
        pathCode,cumDist, tokenChange=checkjunction(pathCode,cumDist)
        piece_place[piece]=(pathCode,cumDist)
        # print(piece, 'piece', piece_place)

        # 3; 현재 말에 대한 새로운 위치 업데이트 '후에'<T>
        # 다른 말 존재 vs 다른 말 부재 => 이동 막기 vs 이동 허가
        otherPlaces=[place for key,place in piece_place.items() if(key !=piece)]
        # print('my place ',(pathCode, cumDist),'others',otherPlaces)
        if((pathCode, cumDist) in otherPlaces):
            # 다시 원래값으로 회귀, 득점은 없으니 맨위 가진 값으로 재갱신될 예정이었으나 아에 해당 case는 제외
            # piece_place[piece]=preserved
            token_duplication=True
        else:
            # 말이 겹치지는 않았지만,새로운 경로 위에 올라간 경우 path 갱신 필요
            if(tokenChange): curPath=path[pathCode]
            Point=curPath[cumDist]

        piece_Points[piece] = Point
        # print(piece, 'piece', piece_Points)
        return token_duplication

if __name__=="__main__":
    T=int(sys.stdin.readline().strip())

    samplespace=list((product(range(1,5),repeat=10)))
    # print(list(product(range(1,3),repeat=3)))
    # [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

    results=[]
    for numT in range(1,T+1):
        # MDs ; 1d vectors, moving distance set
        MDs = list(map(int, sys.stdin.readline().split()))

        maxPoint=-1000000
        # 1 sample, ex) (1,1,1,1,1,1,1,1,1,1)
        for sample in samplespace:
            # reinit the vairables
            piece_place = { piece : (0,0) for piece in pieces}
            piece_Points ={ piece : 0 for piece in pieces}

            # if duplication occurs, token of dup becomes true and the case is dumped

            for idx in range(10):
                piece, MD = sample[idx], MDs[idx] 
                if(piece_place[piece]==(-1,-1)):
                    # token of bad case로 별도 선언하면 의미상 명확하나, 그냥 기존 변수 빌림
                    token_duplication=True
                    break
                token_duplication=simulation(piece, MD)
                if(token_duplication): break
            
            if(token_duplication): pass
            else:
                submax=sum(piece_Points.values())
                if(submax>maxPoint):
                    maxPoint=submax
        results.append((numT,maxPoint))

    for result in results:
        print('#'+str(result[0]),result[1])