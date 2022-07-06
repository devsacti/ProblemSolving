# ps1. comprehension

## Target 최대 랜선의 길이
## binary search

# ps2. applying comupter algorithms

# ps3. impl

def bs(lines,s,e):
    # global k,n
    answer=0
    
    while(s<=e):
        mid=(s+e)//2
        # print(mid)

        cand_n=0
        for line in lines:
            cand_n+=line//mid
        
        if(cand_n>=n):
            answer=mid
            s=mid+1
        else:
            e=mid-1

    return answer

if __name__=="__main__":
    global k,n
    k,n= list(map(int, input().split()))

    lines=[]

    min_line=int(1e100)
    max_line=0

    for _ in range(k):
        line=int(input())

        min_line=min(line,min_line)
        max_line=max(line,max_line)

        lines.append(line)
    
    # print(min_line,max_line)
    lines.sort()
    # print(lines)

    s=1
    e=max_line
    answer=bs(lines,s,e)

    print(answer)