# ps1. comprehension
# 1 base indexing

def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i,j,k = cmd
        
        target_array=sorted(array[i-1:j])
        
        answer.append(target_array[k-1])
    
    return answer