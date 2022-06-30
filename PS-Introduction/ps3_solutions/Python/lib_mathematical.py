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

# gcd, lcm +reduce ; a*b = L*G
from functools import reduce
global_gcd=reduce(lambda x,y:gcd(x,y),li_interval)

# lib that is related with count of cases or bruteforce, recursive
from itertools import product
from itertools import combinations
from itertools import permutations

from string import *
# product cases, combinations cases, permutations cases
samplespace=[i for i in range(1,n+1)]
samplespace2=[char for char in ascii_lowercase]
print(samplespace)
print(samplespace2)

allcases=list(product(samplespace,samplespace2))
#or
totalcases=list(product(samplespace,repeat=3))
print(allcases)

r=3
permutations_cases=list(permutations(samplespace,r))
print(permutations_cases)
print(len(permutations_cases))

combinations_cases=list(combinations(samplespace,r))
print(combinations_cases)
print(len(combinations_cases))
