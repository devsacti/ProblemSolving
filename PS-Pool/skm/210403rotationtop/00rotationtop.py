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

# 이럴 바엔 그냥 push 후 한번 갱신해주는 게 적긴 더 적을듯,

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

    print('# idx r ', idx_r)
    for idx, row in enumerate(valid_coordinates):
        print(idx,row)
    dq_valids=valid_coordinates[idx_r]
    # print(dq_valids)
    if(d==0):
        fx=lambda x: None if x == None else (x+c)%M
        # print('check')
        dq_valids=deque(map(fx,dq_valids))
        for _ in range(c):
            # print('check')
            dq_valids.appendleft(dq_valids.pop())
            print(dq_valids)

    else:
        fx=lambda x: None if x == None else (x-c)%M
        dq_valids=deque(map(fx,dq_valids))
        for _ in range(c):
            dq_valids.append(dq_valids.popleft())

    matrix[idx_r]=dq_seq

    valid_coordinates[idx_r]=dq_valids
    # print(' '.join(seq))

def checkeradjacent( valid_coordinate ):
    global valid_coordinates, updated_valid_coordinates

    global matrix,ck_matrix
    global cnt_remove
    # print('given 좌표 ',valid_coordinate)
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
        
        # print('trial ',idx_r,idx_c,cand_idx_r,cand_idx_c)

        # 오답 결과, 비운다 의 상응해서 기입한 0이 추후 0과 0은 같다로 판단되어,
        # 추후 변화가 없을 시 처리가 진행되지 않았음.
        # + 에라토스 테네스로 아에 하위 if는 비활상회 될 예정이지만, 일단 주석처리
        # if(matrix[idx_r][idx_c]==0):
        #     #현재 위치가 0이란 것은 비운다에 상응하니, 더이상 논의 x
        #     break

        if(matrix[idx_r][idx_c]==matrix[cand_idx_r][cand_idx_c]):
            token_same=True
        
    if(token_same):
        # print('plz remove', idx_r,idx_c)
        ck_matrix[idx_r][idx_c]=1
        updated_matrix[idx_r][idx_c]=0
        # (1,0)을 삭제할 줄 알았는데, 아마도 1행 0 번째를 지운듯하다.
        # 나는 val을 줬는데, 자신의 index로 인식-> 아니다 삭제는 내 생각대로 작동,
        # 근데 그보다 갱신되는 리스트를 계속 참조할때 idx의 문제였음.
        # valid_coordinates.remove( (idx_r,idx_c) )
        # print('--after remove')
        # print(valid_coordinates)
        valid_coordinates[idx_r][idx_c]=None
        cnt_remove+=1
    else:
        #ck_matrix[idx_r][idx_c]=0
        updated_matrix[idx_r][idx_c]=matrix[idx_r][idx_c]
        # 솎아내려고 전체 탐색보단, 그냥 새로운 변수에 추가하자.->push로 이관
        # updated_valid_coordinates.append( (idx_r,idx_c) )
    

def checker_sum_matrix(updated_matrix):
    global valid_coordinates
    global denomimator
    sum_matrix=0

    for row in updated_matrix:
        subsum=sum(row)
        sum_matrix+=subsum

    mean_matrix=sum_matrix//denomimator
    # print('val,mean matrix ',sum_matrix,(N*M),denomimator,mean_matrix)
    # +-1 based on mean
    # for idx_r in range(N):
    #     for idx_c in range(M):
    #         if(updated_matrix[idx_r][idx_c]==0):
    #             pass
    #         else:
    #             if(updated_matrix[idx_r][idx_c]>mean_matrix):
    #                 updated_matrix[idx_r][idx_c]-=1
    #             elif(updated_matrix[idx_r][idx_c]<mean_matrix):
    #                 updated_matrix[idx_r][idx_c]+=1
    #             else:
    #                 pass

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

    print('--갱신된 매트릭스;평균값에 의해--')
    print(*updated_matrix,sep='\n')
    print('----')


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

        print('----처음 탑')
        print(*matrix,sep='\n')
        print(cmds)

        # per Testcase,
        # 에라토스테네스의 체를 방문해야할 좌표들 모음에 적용
        # 처음에는 모든 좌표를 방문해야겠지만 cmd돌면서 불필요한건 없애자
        # valid_coordinates=[(i,j) for i in range(N) for j in range(M)]
        valid_coordinates=[]
        # for i in range(N):
        #     row=[(i,j) for j in range(M)]
        #     valid_coordinates.append(row)

        # 그 와중에 중복되는 값들은 enumerate를 통해서 쓰고, 변수만 저장->연산용이
        for i in range(N):
            row=deque([j for j in range(M)])
            valid_coordinates.append(row)

        for idx, row in enumerate(valid_coordinates):
            print(idx,row)


        #execution; rotate and remove and meancalcul blabla
        for cmd in cmds:
            print('######cmd ',cmd)
            # a means floor, d is direction, c is cnt of rotation
            a,d,c = map(int,cmd)

            # per cmd, ck matrix and updated matrix are needed
            # cuz, per cmd rotation of floor occurs and partially removed matrix occurs
            # however there is no remove, +-1 occurs based on mean 
            ck_matrix=[[0]*M for _ in range(N)]
            updated_matrix=[deque([0]*M) for _ in range(N)]

            std_r=a
            if(std_r==1):
                idx_rs=[(num_floor-1) for num_floor in range(1,N+1)]
            else:
                # 3의 배수 3, 6, 9인 상황에서 이것들이 idx상 각각 -1되야하는것과
                # 2-1의 배수 2,4,6은 다르다. 그러므로 아래 코딩은 잘못됨
                # 이런 걸 피할려면 최대한 있는그대로를 하자
                # idx_rs=[idx_floor for idx_floor in range(N) if N%idx_r==0]

                idx_rs=[(num_floor-1) for num_floor in range(1,N+1) if (num_floor%a==0)]
            
            print('방문해야할 행의 인덱스 ',idx_rs)
            # 해당되는 모든 행이 d 방향으로, c 칸만큼
            # 컴퓨터상에선 행별 변화는 각기 일어나지만,
            # 요구상 이 모든 것들이 동시에니까, 아래 for문이 다 돈 뒤, 판별,
            for idx_r in idx_rs:
                pushmethod(idx_r,d,c)

            print('--after push--')
            for idx, row in enumerate(valid_coordinates):
                print(idx,row)
            print(*matrix,sep='\n')
            
            #per cmd,which means 1 rotation of floor's'
            #per cmd,now we check the adjacent and remove
            cnt_remove=0
            # for idx_r in range(N):
            #     for idx_c in range(M):
            #         checkeradjacent(idx_r,idx_c)
            
            #!! valid한 좌표만 돌자, 한편, checker adjacent에서 또 솎아내서
            # 다음 cmd에서는 솎아낸 좌표만 돌고,
            print('--before checking adjacent, valids--')
            print(*valid_coordinates,sep='\n')
            # print('--before checking adjacebt, updated--')
            # print(updated_valid_coordinates)

            for idx_r,row in enumerate(valid_coordinates):
                for idx_c in row:
                    if( idx_c == None):
                        pass
                    else:
                        checkeradjacent( (idx_r,idx_c) )

            for idx, row in enumerate(valid_coordinates):
                print(idx,row)
                
            print('--after checking adjacent;주변이랑 같아서--')
            print(*updated_matrix,sep='\n')
            # print(updated_valid_coordinates)
            # update the valid
            # valid_coordinates=valid_coordinates[:]

            print('--삭제 수--')
            print(cnt_remove)
            #삭제에 따른 분모 수 갱신
            denomimator=denomimator-cnt_remove
            print('--체크 매트릭스--')
            print(*ck_matrix,sep='\n')


            #per cmd, check no remove or not
            if(cnt_remove==0):
                # reupdate the updated matrix with calcul mean
                checker_sum_matrix(updated_matrix)
            else:
                #go to next cmd
                pass

            #renew the matrix for next cmd
            matrix=copy.deepcopy(updated_matrix)

        
        #find the sum of matrix after all cmd
        # print(*matrix,sep='\n')

        sum_final=0
        for row in matrix:
            sub=sum(row)
            sum_final+=sub
        
        # print('#'+str(int(T)+1),sum_final)
        sum_finals.append(sum_final)
    

    for idx,sum_final in enumerate(sum_finals):
        print('#'+str(idx+1),sum_final)




