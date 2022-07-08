import sys

def update_cur( curR, curC):
    global N,M,matrix,updated_matrix
    global dir_vectors
    global k

    # print('current ', curR, curC, matrix[curR][curC])
    # current 의 주변 index 받기
    adjacent_idxs=[]

    for vector in dir_vectors:
        cand_r=curR+vector[0]
        cand_c=curC+vector[1]

        if( cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>M-1):
            continue
        
        adjR, adjC = cand_r, cand_c
        adjacent_idxs.append( (adjR, adjC) )
    # print(adjacent_idxs)

    cnt = len(adjacent_idxs)
    # spread cur value to adjacent
    # print('denominator',(2*(k*k)+2*k+1) )
    unit = matrix[curR][curC] // (2*(k**2)+2*k+1)

    # print('unit', unit)
    # val that will be divided is substracted
    updated_matrix[curR][curC]+=-unit*cnt
    # update에는 가중치들끼리만 합산한다.
    for idx_adj in adjacent_idxs:
        # r,c; INDEX OF COMPUTER
        adjR,adjC = idx_adj
        #unit will be stacked so +=
        updated_matrix[adjR][adjC]+=unit
    
    # print(*updated_matrix, sep='\n')

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
    global dir_vectors
    dir_vectors=[]
    for subk in range(1,k+1):
        # print('total',subk)
        for dr in range(0,subk+1):
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
    # print(dir_vectors)

    # during 't' times
    while(t):
        # print('======t======', t)
        updated_matrix=[[0]*M for _ in range(N)]

        # r,c ; INDEX OF COMPUTER
        for r in range(N):
            for c in range(M):
                # only update the delth, except base
                update_cur(r,c)
                # so, update the base
                updated_matrix[r][c]+=matrix[r][c]

        # print(*updated_matrix,sep='\n')
        # print('--')
        
        for idx, row in enumerate(updated_matrix):
            matrix[idx]=row

        # print(*matrix,sep='\n')
        # print('--')
        t-=1
    
    for row in matrix:
        print(' '.join(map(str,row)))