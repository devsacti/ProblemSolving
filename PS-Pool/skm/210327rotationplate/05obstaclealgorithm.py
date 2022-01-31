'''
transpose시킬까 말까, 파이썬의 강점.
복습때 하자, 귀찮지만 col은 조금 복잡하게
참고)파이썬 transpose
>>> A = [[1,2,3],[4,5,6]]
>>> list( zip(*A))
[(1, 4), (2, 5), (3, 6)]

+
빙고처럼 푸는게 직관적이라 일단 답을 금방 구할줄 알았는데
해보니까, 문제명도 robot이고, 로봇객체를 상정하고
1칸씩 탐색 and 값체크, 전진가
더 적절했던 듯, 다음문제부터 반영

90점 나오는데 코드도 쓸데없이 길고, 차라리 새로 재귀 또는 dfs형태로 짜서
다음문제 풀고 그걸로 돌아오자

'''

from collections import deque

def obstaclechecker(startyx, endyx):
    global matrix
    #
    starty, startx=startyx
    endy, endx=endyx

    #각각 x축상, y축상 이동
    if(starty==endy):
        #y constant, x variable
        xidx_obstacle=-1

        xlefttoken=0

        #x가 감소 시 range(startx, endx+1)이 먹통, 반영 필요,
        if(startx>=endx):
            #x 감소의 경우, 육안상 left
            xlefttoken=1
            section=[x for x in range(startx,endx-1,-1)]
        else:
            #x 증가의 경우, 육안상 right
            xlefttoken=0
            section=[x for x in range(startx,endx+1)]        

        for x in section:
            element=matrix[endy][x]
            if(element==-1):
                xidx_obstacle=x
            
        if(xidx_obstacle!=-1):
            #-1's index is catched
            if(xlefttoken==1):
                #
                return endy, (xidx_obstacle+1)

            else:
                #
                return endy, (xidx_obstacle-1)

        else:
            return endy,endx

    elif(startx==endx):
        #y variable, x constant
        yidx_obstacle=-1
        #연산 아닌, 육안기준 down up
        yuptoken=0

        #y가 감소 시 range(starty, endy+1)이 먹통, 반영 필요,
        if(starty>=endy):
            #y 감소의 경우, 육안상 up
            yuptoken=1
            section=[y for y in range(starty,endy-1,-1)]
        else:
            #y 증가의 경우, 육안상 down
            yuptoken=0
            section=[y for y in range(starty,endy+1)]
            # print(section)

        for y in section:
            element=matrix[y][endx]

            if(element==-1):
                yidx_obstacle=y
            
        if(yidx_obstacle!=-1):
            #-1's index is catched
            
            if(yuptoken==1):
                #
                return (yidx_obstacle+1), endx

            else:
                #
                return (yidx_obstacle-1), endx

        else:
            return endy,endx
    else:
        pass


if __name__=="__main__":
    N,M=map(int, input().split())

    global matrix
    matrix=[]

    for _ in range(N):
        row=[]
        matrix.append(list(map(int,input().split())))

    commands=[]
    commands.append(list(map(int,input().split())))
    # print(*matrix,sep='\n')
    # print(commands)

    dq_commands=deque(commands)

    while( len(dq_commands)>0 ):
        # (y,x), row->y, col->x 행렬 맞춤형 idx, xy좌표계로 치환하다가 만나니까 헷갈림,
        # d direction
        # r ?, range
        y,x,d,r=dq_commands.popleft()

        #d 가 0 이면 오른쪽, 1 이면 왼쪽, 2 면 아래, 3 이면 위
        if(d==0):
            #x right
            candi_x=x+r

            startyx=(y,x)
            endyx=(y,candi_x)

            y,x=obstaclechecker(startyx, endyx)

        elif(d==1):
            #x left
            candi_x=x-r

            startyx=(y,x)
            endyx=(y,candi_x)

            y,x=obstaclechecker(startyx, endyx)

        elif(d==2):
            # 육안상 y down, but mathetically increment of y coordinate,
            # 행렬에 xy좌표계를 그대로 연결짓게할려고 yx로 한것같긴한데,
            # 결국 이 방법도 이런 모순적인 상황 직면, 그냥 회전으로 이해해야하는 게 아닐까
            candi_y=y+r

            startyx=(y,x)
            endyx=(candi_y,x)

            y,x=obstaclechecker(startyx, endyx)

        elif(d==3):
            #y up ,x constant
            candi_y=y-r

            startyx=(y,x)
            endyx=(candi_y,x)

            y,x=obstaclechecker(startyx, endyx)
        else:
            pass

    
    print(matrix[y][x])


