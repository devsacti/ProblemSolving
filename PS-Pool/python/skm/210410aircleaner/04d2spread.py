import sys


def update_cur( cur_r, cur_c):
    global N,M,matrix,updated_matrix

    # print('current ', cur_r, cur_c)
    # current 의 주변 값 받기
    adjacent_vals=[]

    dr=[0,0,1,-1]
    dc=[1,-1,0,0]

    for d in range(4):
        cand_r=cur_r+dr[d]
        cand_c=cur_c+dc[d]

        if( cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>M-1):
            continue

        adjacent_vals.append(matrix[cand_r][cand_c])

    # print(adjacent_vals)
    
    updated_matrix[cur_r][cur_c]=matrix[cur_r][cur_c]+sum(adjacent_vals)


if __name__=="__main__":
    global N,M
    N,M=map(int,sys.stdin.readline().split())

    global matrix, updated_matrix
    matrix=[]
    for _ in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        matrix.append(row)
    

    t=int(sys.stdin.readline().strip())

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