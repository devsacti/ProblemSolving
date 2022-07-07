from collections import defaultdict
from functools import reduce

def solution(clothes):
    answer = 0
    
    kind_clothes=defaultdict(list)
    
    for item in clothes:
        name, kind = item        
        kind_clothes[kind].append(name)
    
    cnt_items = [len(val) for val in kind_clothes.values()]
    cnt_items = list(map(lambda item : item +1, cnt_items))
    
    answer = reduce(lambda pre,post : pre * post, cnt_items)
    answer-=1
    
    return answer