## lib
#basic
import string
#ascii_lowercaseList=string.ascii_lowercase

from math import *

# max, min, abs
min(-5, 3, 0, 3, -5, key=abs)
max(nums, key=abs)

sqrt(x)
# x**(1/2)

# gcd, lcm +reduce ; a*b = L//G
from functools import reduce
global_gcd=reduce(lambda x,y:gcd(x,y),li_interval)

# lib that is related with count of cases or bruteforce, recursive
from itertools import product
from itertools import combinations
from itertools import permutations

from string import *
# product cases, combinations cases, permutations cases
sample=[i for i in range(1,n+1)]
sample2=[char for char in ascii_lowercase]
print(sample)
print(sample2)

allcases=list(product(sample,sample2))
#or
totalcases=list(product(sample,repeat=3))
print(allcases)

r=3
permutations_cases=list(permutations(sample,r))
print(permutations_cases)
print(len(permutations_cases))

combinations_cases=list(combinations(sample,r))
print(combinations_cases)
print(len(combinations_cases))
