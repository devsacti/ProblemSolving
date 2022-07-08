'''
1 2 3 4 5

2 1 2 3 2 4 2 5

3 3 1 1 2 2 4 4 5 5

'''

def solution(answers):
    answer = []
    
    val_one=[1,2,3,4,5]
    val_two=[2,1,2,3,2,4,2,5]
    val_three=[3,3,1,1,2,2,4,4,5,5]
    
    cnt_one=0
    cnt_two=0
    
    cnt_three=0
    
    idx_one=0
    idx_two=0
    idx_three=0
    
    
    for answer in answers:
        # print(answer)
        if answer==val_one[idx_one]:
            cnt_one+=1
        
        idx_one+=1    
        idx_one %= len(val_one)
        
        if answer==val_two[idx_two]:
            cnt_two+=1
        
        idx_two+=1    
        idx_two %= len(val_two)
        
        if answer==val_three[idx_three]:
            cnt_three+=1
        
        idx_three+=1    
        idx_three %= len(val_three)
    
    # print(cnt_one,cnt_two,cnt_three)
    
    # dict
    record={k:v for k,v in zip(range(1,4),[cnt_one,cnt_two,cnt_three])}
    # print(record)
    
    # max
    std = max([cnt_one,cnt_two,cnt_three])
    
    record=sorted(record.items(), key = lambda item:item[1], reverse = True)
    # print(record)
    
    answer = []
    for item in record:
        key,val = item
        if(val==std):
            answer.append(key)
    # print(answer)
    return answer