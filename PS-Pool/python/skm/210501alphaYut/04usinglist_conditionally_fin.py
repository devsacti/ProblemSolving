# 제출용
import sys

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
        cumDist+=num
        # 의도된 자료형태 상, 누적 거리가 현재 경로의 길이를 벗어나면 
        # 목표점에 도달한 것으로 보고 처리 및 break
        if(cumDist>=len(curPath)-1):
            cumPoint+=curPath[-1]
            print(curPath[-1])
            break

        cumPoint+=curPath[cumDist]
        print(curPath[cumDist], end=' ')
        
        # step2 ; 현재 경로 상 위치에서 경로 유지 또는 변경 파악
        # token of checking change of path
        tokenChange=False
        tokenChange, row=checkjunction(cumDist, row)
        # print('next changing path ?', tokenChange)
        if(tokenChange):
            cumDist=0
            curPath=path[row]
        else:
            pass