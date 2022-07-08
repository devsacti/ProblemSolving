import sys

if __name__=="__main__":
    n=int(sys.stdin.readline().strip())
    nums=sys.stdin.readline().split()
    checklist=['0']*n

    idx_check=0
    while(idx_check<=(n-1)):
        token_same=False
        idx_left_adjacent=idx_check-1
        idx_right_adjacent=idx_check+1

        if(idx_left_adjacent<0):
            pass
        else:
            if(nums[idx_check]==nums[idx_left_adjacent]):
                token_same=True

        if(idx_right_adjacent>(n-1)):
            pass
        else:
            if(nums[idx_check]==nums[idx_right_adjacent]):
                token_same=True
            
        if(token_same):
            checklist[idx_check]='1'

        idx_check+=1
    
    # print(checklist)
    print(' '.join(checklist))