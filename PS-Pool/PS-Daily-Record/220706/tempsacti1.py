from math import *

def recursive(sample,idx_k,n,result):
    # print('cur result',result)
    # print('cur n',n)
    if(len(sample)!=0):
        # print('cur candidates',sample)
        # print('idx ',idx_k)
        divide_unit=factorial(n-1)
        # print('divide unit',divide_unit)
        target_idx=idx_k//divide_unit
        result.append(sample[target_idx])
        del sample[target_idx]

        next_idx=idx_k%divide_unit

        # print('##',next_idx)
        recursive(sample,next_idx,(n-1),result)


if __name__=="__main__":
    n,k=map(int,input().split())

    samplespace=[val for val in range(1,n+1)]

    sample=samplespace[:]
    result=[]

    idx_k=k-1

    recursive(sample,idx_k,n,result)

    print(result)