from collections import deque

if __name__=="__main__":
    n,q=map(int,input().split())
    seqs=list(map(int,input().split()))
    
    command=[]
    for case in range(q):
        command.append(list(map(int,input().split())))

    # print(n,q, seqs,command)

    dq_command=deque(command)
    
    curx=0
    while( len(dq_command) >0 ):
        d, y=dq_command.popleft()
        # print(d,y)
        if(d==1):
            #
            print( ( seqs[(curx+(y))%n] ))
            curx=(curx+(y))%n
        elif(d==2):
            #
            print( ( seqs[(curx-(y))%n] ))
            curx=(curx-(y))%n