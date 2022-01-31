'''
reference link : https://programmers.co.kr/learn/courses/30/lessons/77486

ps3. Impl
vector 형태의 tree로 구현 예정
=> 해도 생각해보니까, 결국은 dfs는 동일하게 1000번을 넘는 반복호출로 런타임이 뜨게 되있었음
=> 근데 참고자료를 바탕으로 바꿔보니까, 내꺼 재귀랑 다를바없음,
 다만 if문이 위쪽이라 한두번 더 호출되는 정도일텐데, 바꾸니까 통과함, 한두번 더 호출되서 런타임 에러 뜬 듯함
link plus refers : https://programmers.co.kr/learn/courses/30/lessons/77486

'''
from collections import defaultdict
    
def dfs(now,revenue):
    global reversed_tree,dict_name_result
    if(now == "center"):
        return
    if(revenue == 0):
        return
    
    # 버림 => 부모에게 줄 것의 소수점을 버리되, 버린 소수점을 가질거에 붙여서 정수화
    # cutting(untrailed_revenue) 대신 revenue // 10 도 가능
    willgive_revenue=revenue//10
    get_revenue=revenue-willgive_revenue
    # print('now',now,'get',get_revenue,' willgive',give_revenue)
    # print()
    dict_name_result[now]+=(get_revenue)
    
    # tree 기준 현재 now의 parent
    parent=reversed_tree[now]
    dfs(parent, willgive_revenue)
    
def solution(enroll, referral, seller, amount):
    # from adjacent tree to vector tree
    # reversed_tree=defaultdict(list)
    # tree=defaultdict(list)
    global reversed_tree
    reversed_tree=defaultdict(str)
    tree=defaultdict(str)
    
    for child,parent in zip(enroll,referral):
        if(parent=="-"):
            # 이해와 대조를 위한 tree
            tree["center"]=child            
            # 역트리
            reversed_tree[child]="center"
        else:
            tree[parent]=(child)
            reversed_tree[child]=(parent)
    
    # keys=list(reversed_tree)
    # for key in keys:
    #     print(key,',', reversed_tree[key])
    # print()

    # center는 제외한, 판매원별 수익
    global dict_name_result
    # 테스트 결과 초기값은 0이다.
    dict_name_result={name:0 for name in enroll}
    
    for seller,amount in zip(seller,amount):
        # tree 기준 child
        child=seller
        revenue=amount*100
        dfs(child,revenue)
    # print(dict_name_result)
    answer = [val for val in dict_name_result.values()]
    # answer=[]
    return answer