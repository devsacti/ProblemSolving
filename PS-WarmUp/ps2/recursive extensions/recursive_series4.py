'''
ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern
pattern1.
factorial and bruteforce

pattern2.
factorial custom

ps2. applying computer algorithms to problem
ps2.1. utilizations

recursive and backtracking

ps2.2. integrations

ps3. Impl
'''

# control of recursive ; estimate promising or not => 0 or -1, if promising, then check fit or not (-1 or 1), and  keep (0) 
def promising(depth,limit,result):
    print(depth,limit,result,end='=> ')
    global samplespace, results

    promising=False
    if(depth<=1):
        promising=True
    else:
        if(all( x1+1==x2 for x1,x2 in zip(result[:depth-1],result[1:depth]))):
            promising=True

    print(promising)
    if(promising):
        if(depth>=limit):
            
            if(limit==1 and result[0]==1):
                # 1!는 1 이다.
                return 1

            if(result[0]==1 and result[depth-2]+1==result[depth-1]):
                return 1
            else:
                return -1
        else:
            return 0
    else:
        return -1

# recursive for factorial, original version
def recursive_factorial(depth,limit,result):
    global samplespace, results
    print('cur depth',depth,'result ',result, end=" => ")
    
    # backtracking part
    # token means 1,0,-1 which is success, not success(but promising), not success(and unpromising)
    token_ctrl=promising(depth,limit,result)
    print('# token_ctrl ',token_ctrl)
    
    if(token_ctrl == 1):
        # print('success ',result)
        results.append(result)
    elif(token_ctrl == 0):
        for idx_fork,val_fork in enumerate(samplespace):
            result[depth]=val_fork
            recursive_factorial(depth+1,limit,result[:])
            result[depth]='*'
    else:
        pass

if __name__=="__main__":
    n=int(input())
    global samplespace
    samplespace=[item for item in range(1,11)]
    
    depth=0
    limit=n
    
    result=['*' for _ in range(n)]
    global results
    results=[]
    
    recursive_factorial(depth,limit,result)
    print(results)
    
    # for result in results:
    #     answer=1
    #     for item in result:
    #         answer*=item
    #     print(answer)