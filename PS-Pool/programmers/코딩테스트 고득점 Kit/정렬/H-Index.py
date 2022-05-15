# ps1. comprehension
# !! h값은 꼭 리스트에 있는 값일 필요없다! 좁게 해석하지 말자

# ps2. applying algorithm
# 글에 언급되는 것은 모두 변수화해라 ; satisfied, unsatisfied

# ps3. impl

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    len_citations=len(citations)
    # print(len_citations)
    # print(citations)
    for cand_h in range(citations[0],0,-1):
        # print('if h is',cand_h, end=', ')
        satisfied=0
        for item in citations:
            # print(item, end=' ')
            if(item>=cand_h):
                satisfied+=1
            
        if satisfied>=cand_h:
            answer=cand_h
            break
                
        # print('cnt_satisfied',satisfied)
    
    return answer