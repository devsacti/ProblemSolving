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

# curRow, cumDist가 사실상 row와 column 역할
# curRow ; dict , simular with above
piece_curRow = { piece : 0 for piece in pieces}
# curPath; dict , simular with above
piece_curPaths= { piece : path[piece_curRow[piece]] for piece in pieces}

# piece_cumDists ; dict , piece : cumDist , cumulative dist
piece_cumDists ={ piece : 0 for piece in pieces}
# piece_Points ; dict , piece : Point 
piece_Points ={ piece : 0 for piece in pieces}

# piece to place(=row&cumdist) ; dict, for 선행 말 탐색용
curRows=piece_curRow.values()
cumDists=piece_cumDists.values()
places=zip(curRows,cumDists)
piece_place = { piece : place for piece , place in zip(pieces,places)}

def checkjunction(curDist, row):
    # 분기점 이후 경로들, part 1~2
    # 유지 시 리턴 값의 default
    tokenChange, row=False, row

    if(row==0 and curDist==5):
        tokenChange=True
        row=1
    elif(row==0 and curDist==10):
        tokenChange=True
        row=2
    # sub of part 1
    if(row==1 and curDist==3):
        tokenChange=True
        row=11
    
    return tokenChange, row

# 장기말(piece) 별로, 이동해야할 칸수를 입력받아 결과를 장기말별 딕셔너리에 저장
def simulation(piece, MD):
    curRow = piece_curRow[piece]
    curPath = piece_curPaths[piece]
    
    cumDist = piece_cumDists[piece]
    Point = piece_Points[piece]
    
    # print(piece, 'piece', cumDist)

    # step1 ; 현재 경로 상 누적 이동거리에 따른 방문 및 점수 획득
    cumDist+=MD
    # step1.5 ; 현재 경로 리스트의 맨끝 인덱스에 도달 = 목표점 도달, 종료
    if(cumDist>=len(curPath)-1):
        Point=curPath[-1]

        #update the relatives
        piece_cumDists[piece] = cumDist
        piece_Points[piece] = Point
        # print(curPath[-1])
        return
    
    # step 2 ; 새로운 위치 업데이트 '전에'
    # 다른 말의 존재 유무에 따라 -1 또는 좌표값 업데이트
    if((curRow,cumDist) in piece_place.values()):
        Point = -1
    else:
        Point=curPath[cumDist]
    # print(curPath[cumDist], end=' ')
    
    # step3 ; 현재 경로 상 위치에서 경로 유지 또는 변경 파악
    # token of checking change of path
    tokenChange=False
    tokenChange, curRow=checkjunction(cumDist, curRow)
    # print('next changing path ?', tokenChange)
    if(tokenChange):
        cumDist=0
        curPath=path[curRow]
    else:
        pass

    piece_curRow[piece] = curRow
    piece_curPaths[piece] = curPath
    piece_cumDists[piece] = cumDist
    piece_Points[piece] = Point
    piece_place[piece] = (curRow,cumDist)

if __name__=="__main__":
    T=int(sys.stdin.readline().strip())

    maxPoint=-1000
    for idxT in range(T):
        # MDs means Moving Distance set
        MDs=map(int,sys.stdin.readline().split())
        corresPiece=map(int,sys.stdin.readline().split())

        cases=list(zip(corresPiece,MDs))
        
        # reinit the vairables
        piece_curRow = { piece : 0 for piece in pieces}
        piece_curPaths= { piece : path[piece_curRow[piece]] for piece in pieces}
        piece_cumDists ={ piece : 0 for piece in pieces}
        piece_Points ={ piece : 0 for piece in pieces}

        for case in cases:
            piece, MD = case 
            simulation(piece, MD)
        # print(piece_Points)

        submax=sum(piece_Points.values())
        if(submax>maxPoint):
            maxPoint=submax
    
    print(maxPoint)