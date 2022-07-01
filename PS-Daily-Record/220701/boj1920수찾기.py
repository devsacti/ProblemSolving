# Source : https://www.acmicpc.net/problem/1920

# ps1. comprehension

# ps2. applying computer algorithms

# ps3. impl

def bs(items,s,e,target):

    search_token=False
    while s<=e:
        mid=(s+e)//2

        if(items[mid]==target):
            search_token=True
            return 1
            
        elif(items[mid]<target):
            s=mid+1
        else:
            e=mid-1

    if(search_token==False):
        return 0           

if __name__=='__main__':
    n=int(input())
    items=list(map(int,input().split()))

    m=int(input())
    cands=list(map(int,input().split()))
    # print(items, cands)

    items.sort()

    # 시간초과남, python in은  bruteforce 급인듯
    # for cand in cands:
    #     if(cand in items):
    #         print('1')
    #     else:
    #         print('0')

    for cand in cands:
        s=0
        e=n-1
        print(bs(items,s,e,cand))