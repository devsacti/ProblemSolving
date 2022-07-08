# 숫자 조합2
# 오전 10:54 2021-05-01
# sum
# using itertools with reminding recursive

from itertools import product
import sys

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())

    # print(list(product(range(1,N+1),repeat=3)))
    for item in list(product(range(2),repeat=N)):
        print(' '.join(map(str,item)))
