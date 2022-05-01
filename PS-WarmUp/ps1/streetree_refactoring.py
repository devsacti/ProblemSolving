# ps1 ; comprehension about problem
# ps1.1.
# ps1.2.

# ps2 ; drawing pattern and exception
# ps2.1.
# ps2.2.

# ps3 ; Impl
from math import *
from functools import reduce

def test():
    pass

if __name__=="__main__":
    n=int(input())

    li_tree=[]

    for _ in range(n):
        li_tree.append(int(input()))

    # print(li_tree)

    li_interval=[]

    for idx in range(1,n):
        li_interval.append(li_tree[idx]-li_tree[idx-1])

    # print(li_interval)

    global_gcd=reduce(lambda x,y:gcd(x,y),li_interval)

    # print(global_gcd)

    answer=0

    for item in li_interval:
        answer+= item//global_gcd -1

    print(answer)