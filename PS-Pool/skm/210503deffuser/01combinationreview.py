# 조합 복습
# 오후 3:24 2021-05-03
# 조합이라는데 product

import sys
from itertools import product

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    
    for item in list(product(range(2),repeat=N)):
        print(' '.join(map(str,item)))