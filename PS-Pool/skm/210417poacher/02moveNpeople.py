# N명 이동
import sys

if __name__=="__main__":
    N,M,k,t = map(int, sys.stdin.readline().split())

    matrix=[[0]*M for _ in range(N)]

    # k is correspods with cnt of human
    humans=[]
    for _ in range(k):
        human= map(int, sys.stdin.readline().split())
        humans.append(human)

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    for human in humans:
        # print('# ',human)
        r,c, d,f = human

        #idx_~ : INDEX OF COMPUTER
        idx_r, idx_c =r-1, c-1

        # t is correspond with cnt execution of 'f' move
        for _ in range(t):
            
            # range(f) means '1' move from 'f' move
            for _ in range(f):
                cand_r=idx_r+dr[d]
                cand_c=idx_c+dc[d]

                if(cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>M-1):
                    break

                idx_r, idx_c =cand_r, cand_c
                # print('$$', idx_r, idx_c)

        print(idx_r+1, idx_c+1)
