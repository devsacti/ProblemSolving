# ps1.

## ps1.2
## dfs를 수단이나 과정말고 결과를 이해하는 데 활용
## dfs로 구현했다고 하면, 주어지거나 전처리를 통해 자료구조화된 노드, 간선, 그래서 트리나 그래프 등의 개념이 전제되나 아래는 너무 추상적
## 단, 구현은 Recursive

# ps2.

# ps3.

# ps4.
# 프로그래머스 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

# global ; answer
def recursive(depth,limit, result,target):
    global answer, nums
    
    if depth == limit:
        if result == target:
            answer += 1
        return
    else:
        recursive(depth+1, limit,result+nums[depth],target)
        recursive(depth+1, limit,result-nums[depth],target)

def solution(numbers, target):
    global answer, nums
    answer = 0
    nums=numbers[:]
    
    depth=0
    limit=len(numbers)
    result=0
    # list
    progress_result=[]
    
    recursive(depth,limit,0,target)
    
    return answer
