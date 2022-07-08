import sys

if __name__=="__main__":
    N,M,q = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    cmds=[]
    for _ in range(q):
        cmd=map(int, sys.stdin.readline().split())
        cmds.append(cmd)

    curR, curC = 0,0
    for cmd in cmds:
        # print(cmd)
        # d direction, r is magnitude of component of vector
        d, r = cmd
        
        dr=[0,0,1,-1]
        dc=[1,-1,0,0]

        while(r):
            cand_r = curR+dr[d]
            cand_c = curC+dc[d]

            if(cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>M-1):
                break

            if(matrix[cand_r][cand_c]==-1):
                break

            curR=cand_r
            curC=cand_c
            r-=1
        print(matrix[curR][curC])
