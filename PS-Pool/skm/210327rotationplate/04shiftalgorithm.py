from collections import deque

if __name__=="__main__":
    N,M=map(int, input().split())

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
        # (y,x), row->y, col->x 행렬 맞춤형, xy좌표계로 치환하다가 만나니까 헷갈림,
        # d direction
        # r ?, range
        y,x,d,r=dq_commands.popleft()

        #d 가 0 이면 오른쪽, 1 이면 왼쪽, 2 면 아래, 3 이면 위
        if(d==0):
            #right
            x+=r
        elif(d==1):
            #left
            x-=r

        elif(d==2):
            #down
            y+=r
        elif(d==3):
            #up
            y-=r
        else:
            pass

    
    print(matrix[y][x])


