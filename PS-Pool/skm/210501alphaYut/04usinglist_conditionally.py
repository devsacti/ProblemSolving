# N번의 이동
# 오전 11:20 2021-05-01
# summary
# what is best datastructure? list or graph...
# regarding that there is no input of Nodes, list is intended insignificantly
# if graph was intended, which means complex datastructure, at least input should be given
# 자료 정의하고 보니까 갈래별로 데이터 저장하면 tree 형태인듯

# lesson 1; 감은 오지만 큰 그림은 안그려지는 모듈은 걍 유치하게 다 쪼개버리자
# 분기점 도달 확인 모듈 필요-> 5단위 3단위 통합 모듈?, 복잡...
# 그러면 그냥 50, 100, 300별 모듈 3개 만들고 추후 통합

# lesson 2; 경로 전환 시, 누적인덱스의 초기화 필요+ 경로별 분기조건도 바꿔야함
# 가령, 현재 path0을 기준으로 분기조건을 짯음, 누적이동이 5와 8일때
# 근데, 5가 나와서 경로 변경 시, 8이 아니라 '새 경로와 3'에 대해서 action을 걸어야함
# cumDist에 추가적인 처리를 통해서 part0기준 분기를 할수는 있긴함, 근데 이러면 경로 2개 씩 생각해서 변수 쪼개거나 처리해야함, 개복잡
# 경로별로 번호 부여해서 경로별 and 새로나온 눈금 수로 조건 변경

# 애당초 자료구조를 마치 기찻길을 확장해나가는 상상하고
# cur path를 새롭게 정의해나가서, cumDist를 좀더 편하게 쓸수도

# tcp 1
# 7
# 5 2 4 4 2 4 3
# 50 250 75 95 1000
# 인덱스랑 입력값 관계 '그냥' 맞겠거니 냅두고, 임시방편으로 해결해서
# 인덱스로 인한 문제 30점 중 20점은 해결했지만, '그냥'으로 인해 10점 해결방법을 못찾음...
# 힘내자! 꼼꼼한 설계와 계획이 바탕이 되야 에러슈팅 가능, 수학 검토랑 동일

import sys

def checkjunction50(cumDist):
    if(cumDist==5):
        #path0 => path10 or path11; 우선 path10할당, 참고로 그 후 3나오면 path11로 전환
        row=1

def checkjunction300(cumDist):
    if(cumDist==8):
        #path1 인상황에서 3이 나오고 통합 8 => path11
        path11=[300,350,400,500,1000]
        curPath=path11

def checkjunction100(cumDist):
    if(cumDist==10):
        #path0 => path10 or path11; 우선 path10할당, 참고로 그 후 3나오면 path11로 전환
        row=2

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
    
if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))

    # part 0
    path0=[0,5,10,15,20,50,30,35,40,45,100,55,60,65,70,75,80,85,90,95,500,1000]
    # part 1
    path10=[50,275,250,300,150,175,75,80,85,90,95,500,1000]
    path11=[300,350,400,500,1000]
    # part 2
    path2=[100,150,125,300,350,400,500,1000]
    # part 3은 path0에 포함되서 무의미

    # row를 통해서 path들을 구분해보자
    # 5 단위의 큰 갈래에 대응하는, path의 row(key)가 대응하도록 설정;0,1,2
    path={ 
        0 : path0,
        1 : path10, 11 : path11,
        2 : path2
    }
    # print(path)
    # summmary of variables
    cumDist=0 # cumulative distance ; cumDist
    nextDist=0 # cumulative distance + current given dist ; nextDist
    
    cumPoint=0
    row =0
    curPath=path[row]

    for num in nums:
        # step1 ; 현재 경로 상 누적 이동거리에 따른 방문 및 점수 획득
        print('cur path ',curPath)
        print(num, cumDist)
        print('--')
        cumDist+=num
        print('total ',cumDist)
        # 의도된 자료형태 상, 누적 거리가 현재 경로의 길이를 벗어나면 
        # 목표점에 도달한 것으로 보고 처리 및 break
        if(cumDist>=len(curPath)):
            cumPoint+=curPath[-1]
            print(curPath[-1])
            break

        cumPoint+=curPath[cumDist]
        print(curPath[cumDist], end=' ')
        print('----')
        
        # step2 ; 현재 경로 상 위치에서 경로 유지 또는 변경 파악
        # token of checking change of path
        tokenChange=False
        tokenChange, row=checkjunction(cumDist, row)
        print('next changing path ?', tokenChange)
        if(tokenChange):
            cumDist=0
            curPath=path[row]
        else:
            pass