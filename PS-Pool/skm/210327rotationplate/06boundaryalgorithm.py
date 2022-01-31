from collections import deque

def robot(cmd):
    global N
    global M
    global matrix

    y,x, d,r =cmd
    # d 
    #         3 y up
    # 1 x left   0 x right,
    #         2 y down,
    # d 0 1 2 3
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]

    #search and move
    while(r>0):
        # print('#',y,x,matrix[y][x])
        #search based on d
        candi_y=y+dy[d]
        candi_x=x+dx[d]

        if(candi_y<0 or candi_y>=N or candi_x<0 or candi_x>=M):
            #whatever others do, if out of range
            # no update and break
            break

        candi_val=matrix[candi_y][candi_x]

        if(candi_val==-1):
            #next room is obstacle
            #no update and break
            break
        else:
            #next room is relavent
            y,x=candi_y,candi_x
        r-=1
    
    return y,x

if __name__=="__main__":
    global N
    global M
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
        # d direction, r ?, range
        finaly, finalx=robot(dq_commands.popleft())
    
    print(matrix[finaly][finalx])