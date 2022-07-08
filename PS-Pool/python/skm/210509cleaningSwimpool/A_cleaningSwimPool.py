# 수영장청소 A
# 오후 2:27 2021-05-09
# core contents ; implicit 4 radix notation
# step of Main
# 1. input
# 2. process of 4 radix notation with itertools.product

import sys
input=sys.stdin.readline
from itertools import product

if __name__=="__main__":
    N,K=map(int,input().split())

    samplespace=[i for i in range(4)]
    productList=list(product(samplespace,repeat=N))
    # print(productList)
    for element in productList[K-1]:
        print(element*90, end=' ')
