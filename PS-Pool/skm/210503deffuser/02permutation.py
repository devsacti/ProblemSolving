# 알파벳순열
# 오후 3:29 2021-05-03
# 순열이라는 데 product

import sys
from itertools import product
import string

if __name__=="__main__":
    n,r = map(int, sys.stdin.readline().split())
    samplespace=string.ascii_lowercase[:n]
    print(samplespace)
    # print(list(product(samplespace,repeat=r)))
    for item in list(product(samplespace,repeat=r)):
        print(''.join(item))