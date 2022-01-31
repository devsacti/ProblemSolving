# 이동 알고리즘 4
# 오후 5:36 2021-05-01
# summary
# ?

# description of datastructer
# main
#  simulation of yut
#   checkingjunction

# lesson 1 다른 말의 존재 유무를 파악할때, 말 별 위치 딕셔너리 외에도
# 경로별 visited로 간소화 가능해보이는데, 딕셔널리 컴프리헨션이 너무 강력함

# tcp1 ; 주어진 현상에 최대한 대응하는 자료구조를 설정하려(제외된 말? => 냅두지 말고, 따로 빼든 완주 토큰 삽입)
# 왠만큼 한것같은데, 30점임, 지금 아에 처음부터 변수정리겸 정리하다보니까
# 왠지 목표지점을 벗어나서 도달한 얘들의 좌표가, 여전히 남아서 후속 말들의 득점에 오차발생시키는 듯함

# tcp2 ; Sol) 비판적으로 문제흐름에 따라가자(=나의 접근논리 미흡), move-> search <F>, move-> update Coord -> search Dup <T>
# 문제에 포괄적으로 명시적인 건 전자뿐인데, 그 사이에 업데이트가 우선되야함
# 해보니까, 새 경로 진입 시 이전 값을 챙기느라 약간 틀어진거였는데, 여튼 보다 올바른 큰틀에서 수정하기로

# tcp3 ; sol. 정상 문제조건은 당연하고 이상한 문제조건 조차 있는그대로; 중복발생 -> 해당 Test 자체 결과 -1
# 당연히 말 별로 -1인줄알았는데, 중복 발생 시 상황(Test situation) 단위로 종료되고 -1인듯
# 근데 어쨌거나 중복 발생 시, 이동말라고 했는데 난 말 이동시킴

# tcp4 ; 정말 역겨운 가설인데, 만약 500에서 95로 가도록 했어야한다면
# 지나온 길은 못돌아간다던지, end와 검정길의 우선순위라든지 허점투성이 *판이다.
# 근데 만약 500에 화살표가 없다는 것에 집중하면 왜 운좋게 90점으로 튄지 설명이 될지도 모른다는게
# * 같다....
# => 다행히 왠지 이미 윳판 나간 말에 대해선 conitinue를 요구하는 것이었다.

import sys

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
    # 현재 case가 속한 Test 단위에 대한 토큰
    Token_Stop=False

    pathCode, cumDist = piece_place[piece]
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
        # step3 -> step2 ; 현재 경로 상 위치에서 경로 유지 또는 변경 파악 => 최신화가 우선되야, 후속 겹침유무 판단가능
        # checkjunction 내부에서 분기점 도달여부에 따라 입력받은 값그대로 돌려주거나, 변경해서 리턴
        pathCode,cumDist, tokenChange=checkjunction(pathCode,cumDist)
        piece_place[piece]=(pathCode,cumDist)
        # print(piece, 'piece', piece_place)

        # step 2 -> 3; 현재 말에 대한 새로운 위치 업데이트 '전에'<F> '후에'<T>
        # 다른 말의 존재 유무에 따라 -1 또는 좌표값 업데이트
        otherPlaces=[place for key,place in piece_place.items() if(key !=piece)]
        # print('my place ',(pathCode, cumDist),'others',otherPlaces)
        if((pathCode, cumDist) in otherPlaces):
            Token_Stop=True
        else:
            # 말이 겹치지는 않았지만,새로운 경로 위에 올라간 경우 path 갱신 필요
            if(tokenChange): curPath=path[pathCode]
            Point=curPath[cumDist]

        piece_Points[piece] = Point
        # print(piece, 'piece', piece_Points)
        return Token_Stop
    # print('--')
        
        
if __name__=="__main__":
    T=int(sys.stdin.readline().strip())

    maxPoint=-1000
    for idxT in range(T):
        # MDs means Moving Distance set
        MDs=map(int,sys.stdin.readline().split())
        corresPiece=map(int,sys.stdin.readline().split())

        cases=list(zip(corresPiece,MDs))
        
        # reinit the vairables
        piece_place = { piece : (0,0) for piece in pieces}
        piece_Points ={ piece : 0 for piece in pieces}

        # if duplication occurs, token of stop becomes True
        for case in cases:
            piece, MD = case 
            if(piece_place[piece]==(-1,-1)): continue
            Token_Stop=simulation(piece, MD)
            if(Token_Stop): break
        # print(piece_Points)

        if(Token_Stop): submax = -1
        else: submax=sum(piece_Points.values())
        # print(submax)

        if(submax>maxPoint):
            maxPoint=submax
    
    print(maxPoint)