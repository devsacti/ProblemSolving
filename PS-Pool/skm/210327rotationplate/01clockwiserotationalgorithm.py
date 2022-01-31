if __name__=="__main__":
    n=int(input())
    seqs=list(map(int,input().split()))
    idx_s, interval=map(int,input().split())

    # print(n, seqs,idx_s,interval)

    print( ( seqs[(idx_s+(interval))%n] ))