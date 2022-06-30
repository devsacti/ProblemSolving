'''
dfs를 수단이나 과정말고 결과를 이해하는 데 활용 ; 추상적

구현은 recursive라고 생각, dfs의 기본 형태 및 정의에서 너무멀다

dfs는 자료구조화된 노드, 간선, 그래서 트리나 그래프 등의 개념이 전제되나

아래에는 input에 있어 트리(혹은 그래프)가 전혀 없다.
'''

# ps4
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


#bruteforce
def judge(result,depth,inequals):
    window=result[depth-1]+inequals[depth]+result[depth]
    return eval(window)

def bruteforce(result,depth,limit, inequals):
  if(depth>=limit):
    print('arrive')
    # print(result)
  else:
    for numchar in '123456789':
      result[depth]=numchar
      print(' '*depth,end='')
      print('given',result)
      print(' '*depth,end='')
      print('depth',depth)

      if(depth==0):
        bruteforce(result[:],depth+1,limit, inequals)
      
      result[depth]='*'
      print(' '*depth,end='')
      print('remove',result)
      print(' '*depth,end='')
      print('depth',depth)
      print('--')
      
        
      # else:
      #   token=judge(result,depth,inequals)
      #   print(token)
      #   if(token):
      #     bruteforce(result[:],depth+1,limit, inequals)
      #   else:
      #     return