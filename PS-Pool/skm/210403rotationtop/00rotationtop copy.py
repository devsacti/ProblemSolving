import sys
from collections import deque
# import copy
# deepcopy 안 쓰고 슬라이싱 썼더니 40점 급상승....엄청 구리구나
# 한편, 결국 전체 인덱스를 이중폴문으로 돌긴도는데, 0인 부분은 pass나 무시로
# 절반정도의 선택
# deque 대신 list를 기본으로 하니까 20점 추가 상승; 90점

# push에서도 deque안쓰고 슬라이싱했지만 90점

def pushmethod(idx_r,d,c):
    global matrix,M
    c=c%M
    dq_seq=deque(matrix[idx_r])
    # 0 clockwise, 1 counter clockwise
    if(d==0):
        dq_seq.rotate(c)
    else:
        dq_seq.rotate(-c)

    matrix[idx_r]=list(dq_seq)

def pushmethod2(idx_r,d,c):
    global matrix,M
    c=c%M
    # 0 clockwise, 1 counter clockwise
    if(d==0):
        matrix[idx_r]=matrix[idx_r][(M-1)-(c-1):]+matrix[idx_r][:(M-1)-(c-1)+1]
    else:
        # print(matrix[idx_r][(c-1):])
        # print(matrix[idx_r][:(c-1)+1])
        matrix[idx_r]=matrix[idx_r][(c-1)+1:]+matrix[idx_r][:(c-1)+1]



def check_adjacent( valid_coordinate ):
    global matrix
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

        if(matrix[cand_idx_r][cand_idx_c]==0):
            continue

        if(matrix[idx_r][idx_c]==matrix[cand_idx_r][cand_idx_c]):
            token_same=True
        
    if(token_same):
        # ck_matrix[idx_r][idx_c]=1
        updated_matrix[idx_r][idx_c]=0
        cnt_remove+=1
    else:
        #ck_matrix[idx_r][idx_c]=0
        updated_matrix[idx_r][idx_c]=matrix[idx_r][idx_c]

    

def check_sum_plusminus():
    global updated_matrix
    global denomimator
    sum_matrix=0

    for row in updated_matrix:
        subsum=sum(row)
        sum_matrix+=subsum

    mean_matrix=sum_matrix//denomimator

    for idx_r in range(N):
        for idx_c in range(M):
            if( updated_matrix[idx_r][idx_c] == 0):
                continue
            else:
                if(updated_matrix[idx_r][idx_c]>mean_matrix):
                    updated_matrix[idx_r][idx_c]-=1
                elif(updated_matrix[idx_r][idx_c]<mean_matrix):
                    updated_matrix[idx_r][idx_c]+=1
                else:
                    continue

if __name__=="__main__":
    global matrix,updated_matrix

    global cnt_remove
    cnt_remove=0

    global N,M
    global denomimator

    sum_finals=[]
    T=int(sys.stdin.readline().strip())

    for idx_T in range(T):
        # init all the matrix,which means top
        # cmds,which means change of top
        N,M,K = map(int, sys.stdin.readline().split())
        denomimator=N*M

        matrix=[]
        for _ in range(N):
            row=list(map(int,sys.stdin.readline().split()))
            matrix.append(row)
        
        cmds=[]
        for _ in range(K):
            cmd=sys.stdin.readline().split()
            cmds.append(cmd)

        for cmd in cmds:
            # print('--',cmd)
            a,d,c = map(int,cmd)

            # ck_matrix=[[0]*M for _ in range(N)]
            updated_matrix=[[0]*M for _ in range(N)]

            std_r=a
            if(std_r==1):
                idx_rs=[(num_floor-1) for num_floor in range(1,N+1)]
            else:
                idx_rs=[(num_floor-1) for num_floor in range(1,N+1) if (num_floor%a==0)]
            
            for idx_r in idx_rs:
                # pushmethod(idx_r,d,c)
                pushmethod2(idx_r,d,c)

            # print(*matrix,sep='\n')

            cnt_remove=0
            for idx_r in range(N):
                for idx_c in range(M):
                    if( matrix[idx_r][idx_c] == 0):
                        pass
                    else:
                        check_adjacent( (idx_r,idx_c) )

            denomimator=denomimator-cnt_remove

            #per cmd, check no remove or not
            if(cnt_remove==0):
                # reupdate the updated matrix with calcul mean
                check_sum_plusminus()
            else:
                #go to next cmd
                pass

            for idx_r, row in enumerate(updated_matrix):
                matrix[idx_r]=row

        sum_final=0
        for row in matrix:
            sub=sum(row)
            sum_final+=sub
        sum_finals.append(sum_final)
    

    for idx,sum_final in enumerate(sum_finals):
        print('#'+str(idx+1),sum_final)