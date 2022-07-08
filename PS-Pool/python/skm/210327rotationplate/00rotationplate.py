'''
회전판과 로봇
module 01~07로 구성

step1 variable and constant check with logic
 총 L회 로봇을 움직
 회전판은 K개의 칸으로 이루어져 있으며, 각 칸에는 자연수
 ?회전판은 최초인 경우에는 지정된 기준에 따르고, 
 ?여러번 돌린 경우에는 직전 회전 결과를 기준으로 회전판을 돌린다.
 회전 방향의 경우, 1은 시계방향을 나타내고 2는 반시계방향

 (이동 방향, 회전 방향, 회전시키는 칸 수)
 N 1 2 : north, clockwise, movement of ration plate not robot

 !!로봇이 얻는 총 점수와 로봇의 최종위치 (x’, y’)를 출력

 input
2 테스트 케이스 T (1 <= T <= 10), matrix's count

5 6 1 2; N,M,xy; N is cnt of col, M is cnt of row
거지같게 y가 row, x가 col에 대응한다.

0 1 1 2 3
2 5 -1 2 0
10 29 17 -1 3
5 4 7 9 12
11 19 -1 12 4
7 8 9 1 3

3; K칸의 큐
2 4 1; 큐의 구성 값들

3; L, L번 움직인다=L번 큐를 돌림
S 1 2
N 2 1
E 2 5

##다시 매트릭스 변수
5 6 2 5
0 1 1 2 3
2 5 -1 2 0
10 29 17 -1 3
5 4 7 9 12
11 19 -1 12 4
7 8 9 1 3
5
2 5 3 1 0
5
S 1 3
N 1 4
W 2 1
N 1 7
E 1 1
'''

def roationplateNrobot(conditionset):
    #좀더 세련되게 변수들 할당하는 요령이 있을까, 지금은 괜찮은데, 변수가 많아지면..
    N,M,x,y = conditionset[0]
    idx_y, idx_x = y-1, x-1

    matrix=conditionset[1]
    
    K= conditionset[2]
    #update 문제로 여기서 선언 조금 쓰임은 좀 뒷쪽이지만
    idx_q=0
    vals_q= conditionset[3]

    L=conditionset[4]
    cmds=conditionset[5]

    sum_point=0

    global cnt_call

    # print(N,M,x,y)
    # print(*matrix,sep='\n')
    # print(K,vals_q)
    # print(L,cmds)
    # print('-------')

    #current place's point
    sum_point+=matrix[idx_y][idx_x]
    matrix[idx_y][idx_x]=0
    # print('sum_point, idx_yx ',sum_point,idx_y,idx_x)

    #get the vector
    for cmd in cmds:
        # print(cmd)
        d, token_clockwise, interval = cmd        
        
        # d 
        #                3 y up, 'N'orth
        # 1 x left,'W'est               0 x right,'E'ast
        #                2 y down,'S'outh
        if(d=='E'):
            idx_d=0
        elif(d=='W'):
            idx_d=1
        elif(d=='S'):
            idx_d=2
        elif(d=='N'):
            idx_d=3
        # print(d,idx_d, end=' ')

        #   0 1 2 3  idx_d 
        dy=[0,0,1,-1]
        dx=[1,-1,0,0]

        # magnitude
        # print(token_clockwise)
        magnitude=0
        if(token_clockwise=='1'):
            #based on q, idx is moving left, 파이썬 개쩌는 게 음수 인덱스도 받아서 나머지만 하면됨
            # print(check)
            idx_q-=int(interval)
            magnitude=vals_q[(idx_q)%K]
        elif(token_clockwise=='2'):
            #based on q, idx is moving right
            idx_q+=int(interval)
            magnitude=vals_q[(idx_q)%K]
        # print(token_clockwise)

        # print(' mag ',magnitude,end=' ')

        #search and move or stop and get points based on vector
        while(magnitude>0):
            candi_idx_y=idx_y+dy[idx_d]
            candi_idx_x=idx_x+dx[idx_d]

            # checking boundary
            if(candi_idx_y<0 or candi_idx_y>=M or candi_idx_x<0 or candi_idx_x>=N):
                break

            # checking obstacle
            if(matrix[candi_idx_y][candi_idx_x]==-1):
                break
            else:
                idx_y,idx_x=candi_idx_y,candi_idx_x
                sum_point+=matrix[idx_y][idx_x]
                matrix[idx_y][idx_x]=0
                # print('sumpoint ',sum_point)
            magnitude-=1
        # print(' idx_yx',idx_y,idx_x)

    print('#'+str(cnt_call),sum_point,(idx_x+1),(idx_y+1))
    cnt_call+=1

if __name__=="__main__":
    T=int(input())

    global cnt_call
    cnt_call=1

    #어렵게 생각하지말고 1차원 더 늘리면 된다.
    # 가능하면 층위가 보이게 선언

    # 시행별 조건모음, 
    # 파이썬 특성상 이렇게 하는게 논리적으로 명확하게 조건들을 모으는게 편한데 
    # C는 어떻게 하지 입력받는 과정마다 할라나 아니면 struct를 이용할라나? 
    # 나도 클래스로 받는 게 적절할까? 파이썬의 강점을 활용하니까 그냥 리스트로 간단히

    #conditionset의 첫번째는 NMxy, matrix, qsize,qvals, L, cmds
    conditionset_trials=[]

    for _ in range(T):
        conditionset=[]
        N,M,x,y=map(int,input().split())
        conditionset.append([N,M,x,y])

        matrix=[]
        for _ in range(M):
            row=[]
            row=list(map(int,input().split()))
            matrix.append(row)
        
        conditionset.append(matrix)
        
        K=int(input())
        conditionset.append(K)

        vals_q=list(map(int,input().split()))
        conditionset.append(vals_q)

        L=int(input())
        conditionset.append(L)

        cmds=[]
        for _ in range(L):
            cmd=list(input().split())
            cmds.append(cmd)

        conditionset.append(cmds)

        # print(*conditionset,sep='\n')
        conditionset_trials.append(conditionset)

    idx=0

    while(idx<len(conditionset_trials)):
        roationplateNrobot(conditionset_trials[idx])
        idx+=1