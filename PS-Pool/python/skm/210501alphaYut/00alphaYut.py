# 알파윷
# 오전 1:12 2021-05-02
# summary
# core; itertools.product and move algorithm

# lesson 1 ; 문제에서 중복 시, 뒷처리를 명확히 안밝히는 시간낭비말고, 내 가설대로, 틀리면 수정

# lesson 2 ; 시간을 줄이자! 말 간 중복 발생 케이스 제거! 
# 정말 돌아갈까? 라는 염려에도 불구 예제에 대해서 답이 나오는데 정말 기쁘다
# 근데, 문득 왜 앞에서 중복 발생 시 아에 테스트 케이스를 멈춘건지 이제 알겠다

# 위 2 종류의 경우, 백프로 Max가 될 수없으므로 그런 경우를 미리 걸러내는 것이다.
# 근데, 통계적으로야 모든 경우에서 중복이 발생하는 일은 없다고 간주할 것 같긴한데
# 수학적으로 이렇게 중복을 제외하다가 모든 케이스가 제외되는 상황이 없다는 증명은 못하겠다.

# lesson 3 ; greedy는 근사값, bruteforce는 정확한 값
# 처음에는 단순히 말 간 중복 케이스는 명백히 추가득점이 막힌 상황으로서 max로서 자격이 없다(위에서 다른 차원의 문제와 별개로)
# 결과적으론 난 명백히 쓸모없는 케이스를 제외한 bruteforce로 접근한 결과가 되었는데
# 문제는 예제 답안 답과 비교해서, 내 출력값이 '더 큰'것을 발견했다.

# 그리고 별도의 print를 한결과 그 케이스가 타당한것을 확인했다.
# 1
# 5 4 4 4 2 5 2 3 4 3 
# (1, 1, 1, 1, 1, 2, 3, 2, 2, 3)
# [5, 4, 4, 4, 2, 5, 2, 3, 4, 3]
# 여기서 직감적으로 예제출력값은 greedy한 접근 속에서 일부 정답이 제외된것을 느꼈고
# 다른 inattrative case로 이미 윷판을 떠난 말이 또 출현하는 경우였고 이에 대해서
# plus 버전에서 적용하여 구현했더니 예제와 같은 답이 나왔다.

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
                if(piece_place[piece]==(-1,-1)): continue
                token_duplication=simulation(piece, MD)
                if(token_duplication): break
            
            if(token_duplication): pass
            else:
                submax=sum(piece_Points.values())
                # print(submax)
                if(submax>maxPoint):
                    if(submax==2050):
                        print(sample,MDs)
                        print(piece_place)
                        print(piece_Points)
                    maxPoint=submax
        results.append((numT,maxPoint))

    for result in results:
        print('#'+str(result[0]),result[1])