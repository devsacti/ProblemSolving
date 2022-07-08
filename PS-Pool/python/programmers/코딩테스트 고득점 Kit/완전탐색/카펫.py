# ps1. comprehension
# brown은 겉테두리 1줄
# 노란색 격자수가 1이상이므로 1줄짜리 카펫은 없다 - condi_1
# 가로 길이가 세로보다 같거나 길다 - condi_2

# ps1.2 greedy로 접근

# ps2. applying algorithms

# module1 : 가능한 카펫 세로가로 후보 도출
# module2 : 후보에 따른 brown yellow 갯수 도출과 비교

# ps3. impl
from math import *

def solution(brown, yellow):
    answer = []
    
    total=brown+yellow
    
    cand=[]
    
    # div is correspond with width
    # cor_div is correspond with height
    for div in range(1, floor(sqrt(total))+1):
        # condi_1
        if(div==1):
            continue
            
        cor_div=floor(total//div)
        
        rest=total%div
        
        if(rest==0):
            pair=[div,cor_div]
            cand.append(pair)
            
    # print(cand)
    
    # 현재 카펫 가로세로 후보 도출 방식에 따르면 언제나 2번째 값이 1번째 값보다 크거나 같다
    # 이와 condi_2를 연결지어 [height, width]라고 간주한다.
    
    # 
    for pair in cand:
        height, width = pair
        
        # print(height,width)
        
        #
        expected_brown= 2*(height+width)-4
        expected_yellow = total - expected_brown
        
        if expected_brown==brown and expected_yellow==yellow:
            answer=[width,height]
            break
        
    
    return answer