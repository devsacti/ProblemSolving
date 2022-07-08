# ps1. comprehension
# 경우의수
# 0 주어짐, 0이 중복되서 주어짐

# 정렬해서 0은 최대한 사용

# ps2. applying algorithms
## 정렬과 permutations
## 99는 어떤 경우든 98, 989, 9899 등 98 에서 파생되는 숫자들보다 우선해야하고,
## 99에서 파생되는 999, 998은 98 포함 그 다음 파생숫자들보다 우선해야한다.
## 이러한 99의 뿌리는 9이고, 9로 시작하는 원소들은 언제나 8에서 파생되는 값들에 우선순위를 가진다.

## rough 한 가중치 계산을 통한 오차 최소화로도 우선 결과 도출, 근데 NN단표처럼 만큼 정확도 없지만
## 우선은 40점 확보

# ps3. impl
from itertools import permutations

def solution(numbers):
    answer = ''
    
    numbers.sort()
    len_numbers=len(numbers)
    
    # 정렬을 기반으로 0과 1000을 미리 솎아낸다.
    for s in range(len_numbers):
        item = numbers[s]
        if item != 0:
            break
            
    for e in range( (len_numbers-1), -1, -1):
        item = numbers[e]
        if item != 1000:
            break
            
    nums=numbers[s:e+1]
    
    answer+=(len_numbers-1-e)*'1000'
    answer+=s*'0'
    
    # print(answer)
    
    # print(nums)
    
    # 한 자릿수이고 9와 같거나 가까울수록, 앞쪽에 가야 이득이다. 9,1,99 ; 9991
    # 두 자릿수이고 99에 가깝거나 9,1,99,95 ; 9 99 95 1 ; 99 95 9
    
    # print(priority)
    
    # 가중치를 연결 ; 자릿수를 같게 만들고, 원래 자릿수가 짧을 수록 가중치를 준다
    weighted_nums=[]
    for item in nums:
        str_item = str(item)
        # 한자릿수의 경우 최소 3배로 길게해야함
        str_item2 = str_item*3
        # print(str_item2[:3])
        weighted_nums.append( (str_item,int(str_item2[:3])) )
        # li_item = list(str_item[:4])
    
    # print(weighted_nums)
    
    weighted_nums.sort(key=lambda element : (element[1]))
    
    # print(weighted_nums)
    
    for item in weighted_nums:
        val, weight= item
        
        answer = val + answer
    
    return answer