# N번의 이동
# 오전 11:20 2021-05-01
# summary
# what is best datastructure? list or graph...
# regarding that there is no input of Nodes, list is intended insignificantly
# if graph was intended, which means complex datastructure, at least input should be given

# 체크포인트1 ; 1d보단 2d
# 처음에는 그냥 1차원 배열로 길게 적을라고 했지만, 이제보니 분기점이란 게
# 일정하게 존재하는 패턴을 반영해서 2d로 선언
# --
# 하긴 했는데, 해보니까 결국은 예쁜 쓰레기같음. 나름 5로 나눌때 몫과 나머지로
# 2d 접근하면 되긴하는데
import sys

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))

    cur=0
    nodes=[
            [0,5,10,15,20],
            [50,30,35,40,45],
            [100,55,60,65,70],
            [75,80,85,90,95],
            [500,1000,1000,1000,1000]
    ]

    stoptoken=False
    for num in nums:
        if(stoptoken):break
        cur+=num
        row=min(cur//5,4)
        
        col=cur%5
        if(cur//5>4):
            col=4
            stoptoken=True
        print(nodes[row][col], end=' ')