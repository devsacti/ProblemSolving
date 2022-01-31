from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    print(*l)
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)