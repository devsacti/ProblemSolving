# 밀기 알고리즘

import sys
from collections import deque

# 길이가 m인 수열이 n개;col and row
# 질문 수 q 
# 각 질문은 세 정수 f(0번 수열부터 n-1번 수열), x, y
# x가 1 f번 수열을 오른쪽으로 y칸 밀어낸 결과를,
# x가 2 f번 수열을 왼쪽으로 y칸 밀어낸 결과를 출력하여라.

def pushmethod(f,x,y):
    global seqs

    # print('seq ',seqs[f])
    dq_seq=deque(seqs[f])

    if(x==1):
        #pass
        for _ in range(y):
            dq_seq.appendleft(dq_seq.pop())
    else:
        for _ in range(y):
            dq_seq.append(dq_seq.popleft())

    seq=list(dq_seq)
    seqs[f]=seq
    print(' '.join(seq))


if __name__=="__main__":
    n,m,q = map(int, sys.stdin.readline().split())

    seqs=[]
    for _ in range(n):
        seq=sys.stdin.readline().split()
        seqs.append(seq)

    # print(seqs)

    conditions_fxy=[]
    for _ in range(q):
        f,x,y = map(int, sys.stdin.readline().split())
        conditions_fxy.append((f,x,y))

    for fxy in conditions_fxy:
        f,x,y=fxy
        pushmethod(f,x,y)

