import sys
from collections import deque

def pushmethod(f,x,y):
    global matrix

    idx_r=f
    dq_row=deque(matrix[idx_r])

    if(x==1):
        dq_row.rotate(y)
    else:
        dq_row.rotate(-y)
    
    matrix[idx_r]=list(dq_row)
    print(' '.join(map(str, matrix[idx_r])))

if __name__=="__main__":
    n,m,q = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(n):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    cmds=[]
    for _ in range(q):
        cmd=list(map(int, sys.stdin.readline().split()))
        cmds.append(cmd)

    for cmd in cmds:
        f,x,y=cmd
        pushmethod(f,x,y)
    
    # for row in matrix:
    #     print(' '.join(map(str, row)))
