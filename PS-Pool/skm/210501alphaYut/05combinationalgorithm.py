# 조합 알고리즘
# 오후 5:28 2021-05-01
# summary
# product of itertools
import sys
from itertools import product
if __name__=="__main__":
    K=int(sys.stdin.readline().strip())

    samplespace=list((product(range(1,5),repeat=10)))
    print(' '.join(map(str,samplespace[K-1])))