'''
link : https://programmers.co.kr/learn/courses/30/lessons/77486

ps1. comprehesion
ps1.1. analysis

절사란 반올림으로 보인다. 가령, 45의 10프로를 5로 취급, 아닐 시 추후 보완
=> 버림임

칫솔 1개의 이익은 100원으로 고정

enroll의 원소는 자식 부모 순으로 정렬되지 않는다.

ps1.2. drawing pattern, exception
pattern1
reversed_tree, tree를 만들고 이익을 얻은 노드에서 수익을 전파해나간다.

exceptions test 11 ~ 13 ; 런타임 에러
의혹 1 . 
seller에는 같은 이름이 중복해서 들어가있을수있다...
=> 우연인 것 같고, 일단 seller의 중복을 제거해본다.
=> 중복을 제거하면 정답이 산출되던 1~10에서 에러가 난다. 아마도 절삭되는 부분의 오차로 인해보인다....seller의 중복 처리는 제외한다....정말 비생산적이다.
=> 그냥 dfs를 돌릴때, enroll에 없으면 제외해본다. 하나 안하나 차이가 없다...

!! 인접리스트 tree 형태에서 재귀구조가 1000회를 넘겨서 생기는 런타임이었다.....로직은 맞다....
=> 오직 벡터 형태의 tree만 허용되고, 간소화된 자료구조를 바탕으로 recursive를 써야 한도를 넘지 않았따.....
=> 지엽적인 문제...

ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularing computer algorithms

module 1 ; making reversed tree
+ seller 중복 제거

module 2; dfs for traverse and distribute


ps2.2. integration

ps3. Impl
'''
from collections import defaultdict

def cutting(revenue):
    share=revenue//1
    
    return share
    
def dfs(reversed_tree, child,revenue):
    global dict_name_result
    # 버림 => 줄 거의 소수점을 버리되, 그걸 가질거에 붙여서 정수화
    give_revenue=cutting((revenue*(0.1)))
    get_revenue=revenue-give_revenue
    
    if(child=='center'):
        return
    
    dict_name_result[child]+=(get_revenue)
    # tree 기준 현재 child의 parent
    for parent in reversed_tree[child]:
        print('cur child', child, dict_name_result[child], 'parent',parent, give_revenue)
        dfs(reversed_tree, parent, give_revenue)
    
def solution(enroll, referral, seller, amount):
    reversed_tree=defaultdict(list)
    tree=defaultdict(list)
    
    for child,parent in zip(enroll,referral):
        if(parent=="-"):
            # 이해와 대조를 위한 tree
            tree["center"].append(child)            
            # 역트리
            reversed_tree[child].append("center")
        else:
            tree[parent].append(child)
            reversed_tree[child].append(parent)
    
    keys=list(reversed_tree)
    
    # for key in keys:
    #     print(key,',', reversed_tree[key])
    # print()

    # center는 제외한, 판매원별 수익
    global dict_name_result
    dict_name_result={name : 0 for name in enroll}
            
    for seller,amount in zip(seller,amount):
        # tree 기준 child
        child=seller
        revenue=amount*100
        dfs(reversed_tree, child,revenue)
        
    # print(dict_name_result)
    answer = [val for val in dict_name_result.values()]
    return answer