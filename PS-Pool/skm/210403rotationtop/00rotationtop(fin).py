#회전탑

# 없다 라는 것에 대응하여 0을 할당하면서, 추후 연산들에서 원치않는 계산
# 가령, 1. 주변과 동일 여부를 판단할 때 0 == 0 으로 오류
#       2. 평균과 비교해서 +-할때 0은 없다인데, 0에 +-1되는것
#       3. 없다 라는 것은 평균을 구할때 분모에서 제외되야하는데, 존재하는 것으로 카운팅되서 평균이 작아짐

# 물론, 추후 합산을 해야하기 때문에 int로 중간에 넣어둔건데
# (meanwhile, None is also make Typeerror at sum)
# 그렇다면 나의 상징에 대해서 추후 연산 프로세스에 이를 반영해야함
# 즉, 나의 상징에 대해서 염두한 연산 프로세스를 구현하자.

# 한편, 고전적으로 폴문 내에서 기본주기마다 변하는 변수를 생성할때는, 
# 뜬금없는 글로벌 상수가 개입해서 갱신이 안되는 현상을 방지하자.

# 0으로 없다를 상징하고, 그냥 0 만나면 프로세스를 멈추거나 스킵하는 형태는
# 타입 리밋 익시드 뜸, 밀기알고리즘 때문에 뭐든 채워놓기는 해야겠지만

# 에라토스테네스의 체를 활용하자.

# !! idx를 숨긴 파이썬 for문의 은닉된 문제, 
# 만약 지금 in 뒤에 list에서 계속 1개씩 빠지는데 그 아이템이
# 인덱스 이전의 아이템이면 idx도 같이 줄어야 삭제된 아이템 뒤 모두가
# 빠짐없이 출력되겠지만, idx는 그대로이기 때문에 1개를 건너뛰게 됨

# idx를 쓰거나, for문 돌리는 동안에는 삭제안하고, 다 한뒤 삭제해야한느데
# 빠지는 아이템이 언제나 다음 인덱스의 뒤편인 지금 전자도 괜찮아 보이는데,
# 지금 함수 구조상이게 좀 불편해서 후자, 후자에서도 update 변수 갱신 형태로

# push 후에, 에라이토스 테네스 체가 갱신되야하는 문제를 찾음.
# 생각해보자. 유효좌표값들을 행렬에 대응하게 선언해서 push에서 갱신가능하게 접근해보자

# 여차 저차 push에서 유효좌표들도 똑같이 이동시켰는데, None이든 그 비어있는 것을  표현하다보면
# None이든 0이든 ' '든 뭐마다가 if로 걸러서 유효한 애만 작동시킬순있는데, 결국은
# 모든 위치에 대해서 1번은 판단, 물론 그 주변 4번 체크보단 부하가 덜한데,
# 그렇게 효과적이지도 않는 상황

# 이럴 바엔 그냥 push 후 한번 갱신해주는 게 적긴 더 적을듯, 결국 똑같이 40점

import sys
from collections import deque
import copy

def pushmethod(idx_r,d,c):
    global matrix,ck_matrix

    global valid_coordinates
    global M

    dq_seq=matrix[idx_r]
    # 0 clockwise, 1 counter clockwise
    if(d==0):
        for _ in range(c):
            dq_seq.appendleft(dq_seq.pop())
    else:
        for _ in range(c):
            dq_seq.append(dq_seq.popleft())

    dq_valids=valid_coordinates[idx_r]
    if(d==0):
        fx=lambda x: None if x == None else (x+c)%M
        dq_valids=deque(map(fx,dq_valids))
        for _ in range(c):
            dq_valids.appendleft(dq_valids.pop())

    else:
        fx=lambda x: None if x == None else (x-c)%M
        dq_valids=deque(map(fx,dq_valids))
        for _ in range(c):
            dq_valids.append(dq_valids.popleft())

    matrix[idx_r]=dq_seq

    valid_coordinates[idx_r]=dq_valids

def checkeradjacent( valid_coordinate ):
    global valid_coordinates

    global matrix,ck_matrix
    global cnt_remove

    idx_r, idx_c = valid_coordinate

    kinds_direction=4
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    
    token_same=False
    for d in range(kinds_direction):
        cand_idx_r=idx_r+dr[d]
        cand_idx_c=idx_c+dc[d]

        if(cand_idx_r<0 or cand_idx_r>N-1):
            continue

        if(cand_idx_c<0 or cand_idx_c>M-1):
            cand_idx_c=(cand_idx_c+M)%M

        if(matrix[idx_r][idx_c]==matrix[cand_idx_r][cand_idx_c]):
            token_same=True
        
    if(token_same):
        ck_matrix[idx_r][idx_c]=1
        updated_matrix[idx_r][idx_c]=0
        valid_coordinates[idx_r][idx_c]=None
        cnt_remove+=1
    else:
        #ck_matrix[idx_r][idx_c]=0
        updated_matrix[idx_r][idx_c]=matrix[idx_r][idx_c]

    

def checker_sum_matrix(updated_matrix):
    global valid_coordinates
    global denomimator
    sum_matrix=0

    for row in updated_matrix:
        subsum=sum(row)
        sum_matrix+=subsum

    mean_matrix=sum_matrix//denomimator

    for idx_r,row in enumerate(valid_coordinates):
        for idx_c in row:
            if( idx_c == None):
                pass
            else:
                if(updated_matrix[idx_r][idx_c]>mean_matrix):
                    updated_matrix[idx_r][idx_c]-=1
                elif(updated_matrix[idx_r][idx_c]<mean_matrix):
                    updated_matrix[idx_r][idx_c]+=1
                else:
                    pass


if __name__=="__main__":
    global matrix,ck_matrix
    global updated_matrix

    global cnt_remove
    cnt_remove=0

    global N,M
    global denomimator
    
    #update per Testcase
    global valid_coordinates

    sum_finals=[]
    T=int(sys.stdin.readline().strip())

    for idx_T in range(T):
        # init all the matrix,which means top
        # cmds,which means change of top
        N,M,K = map(int, sys.stdin.readline().split())
        denomimator=N*M

        matrix=[]
        # ck_matrix=[['0']*M for _ in range(N)]
        # updated_matrix=[['0']*M for _ in range(N)]
        for _ in range(N):
            row=deque(map(int,sys.stdin.readline().split()))
            matrix.append(row)
        
        cmds=[]
        for _ in range(K):
            cmd=sys.stdin.readline().split()
            cmds.append(cmd)

        valid_coordinates=[]
        for i in range(N):
            row=deque([j for j in range(M)])
            valid_coordinates.append(row)

        for cmd in cmds:
            a,d,c = map(int,cmd)

            ck_matrix=[[0]*M for _ in range(N)]
            updated_matrix=[deque([0]*M) for _ in range(N)]

            std_r=a
            if(std_r==1):
                idx_rs=[(num_floor-1) for num_floor in range(1,N+1)]
            else:
                idx_rs=[(num_floor-1) for num_floor in range(1,N+1) if (num_floor%a==0)]
            
            for idx_r in idx_rs:
                pushmethod(idx_r,d,c)

            cnt_remove=0
            for idx_r,row in enumerate(valid_coordinates):
                for idx_c in row:
                    if( idx_c == None):
                        pass
                    else:
                        checkeradjacent( (idx_r,idx_c) )

            denomimator=denomimator-cnt_remove

            #per cmd, check no remove or not
            if(cnt_remove==0):
                # reupdate the updated matrix with calcul mean
                checker_sum_matrix(updated_matrix)
            else:
                #go to next cmd
                pass

            matrix=copy.deepcopy(updated_matrix)

        sum_final=0
        for row in matrix:
            sub=sum(row)
            sum_final+=sub
        sum_finals.append(sum_final)
    

    for idx,sum_final in enumerate(sum_finals):
        print('#'+str(idx+1),sum_final)




