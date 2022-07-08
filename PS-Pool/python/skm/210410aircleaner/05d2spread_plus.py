import sys

def update_cur( cur_r, cur_c):
    global N,M,matrix,updated_matrix
    global dir_vectors

    # print('current ', cur_r, cur_c)
    # current 의 주변 값 받기
    adjacent_vals=[]

    for vector in dir_vectors:
        cand_r=cur_r+vector[0]
        cand_c=cur_c+vector[1]

        if( cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>M-1):
            continue

        adjacent_vals.append(matrix[cand_r][cand_c])

    # print(adjacent_vals)
    
    updated_matrix[cur_r][cur_c]=matrix[cur_r][cur_c]+sum(adjacent_vals)


if __name__=="__main__":
    global N,M,k
    N,M,k=map(int,sys.stdin.readline().split())

    global matrix, updated_matrix
    matrix=[]
    for _ in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        matrix.append(row)
    
    t=int(sys.stdin.readline().strip())

    # direction vectors 만들기; 
    # 다음에는 복습겸 divsion 로직으로 만들어보기도 하는데, 의미가 있나
    global dir_vectors
    dir_vectors=[]
    for subk in range(1,k+1):
        # print('total',subk)
        for dr in range(0,subk+1):
            '''막연히 거부감 가지지 말고, 계산을 해서 과도하지 않으면 편리한 
            파이썬 라이브러리 써라, 0은 몇번 안나오고, 나와도 기껏해야 4개에 대한
            연산인데 시간은 일부이다.'''
            arrange_li=[]
            arrange_li.append( (+dr,+(subk-dr)) )
            arrange_li.append( (-dr,+(subk-dr)) )
            arrange_li.append( (+dr,-(subk-dr)) )
            arrange_li.append( (-dr,-(subk-dr)) )
            # print(arrange_li)

            # 0 이 component일때 중복 제거
            if( dr ==0 or (subk-dr)==0):
                arrange_li=list(set(arrange_li))
            # print('after', arrange_li)

            dir_vectors.extend(arrange_li)
            # # 1 사분면
            # vector1=(+dr,+(subk-dr))
            # dir_vectors.append(vector1)

            # # 2사분면; 아래 조건 양변 정리한 게, dr != 0 이긴한데..와닿지 않아서 혼용
            # if(dr != -dr): 
            #     vector2=(-dr,+(subk-dr))
            #     dir_vectors.append(vector2)
            # # 4사분면
            # if((subk-dr) != -(subk-dr)): 
            #     vector3=(+dr,-(subk-dr))
            #     dir_vectors.append(vector3)

            # # 3 사분면
            # if(dr!=0 and (subk-dr)!=0):
            #     vector4=(-dr,-(subk-dr))
            #     dir_vectors.append(vector4)

            # # 결과적으로 위 if를 통해서 0이 하나라도 구성요소면 vector는 총 2개 생성,
            # # 아니면 4개 생성

    # print(dir_vectors)

    while(t):
        updated_matrix=[[0]*M for _ in range(N)]

        # below r,c are cumputer index
        for r in range(N):
            for c in range(M):
                update_cur(r,c)

        # print(*updated_matrix,sep='\n')
        # print('--')
        
        for idx, row in enumerate(updated_matrix):
            matrix[idx]=row

        # print(*matrix,sep='\n')
        # print('--')
        t-=1
    
    for row in matrix:
        print(' '.join(map(str,row)))