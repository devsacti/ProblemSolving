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


## algorithm templetes
#bruteforce
def judge(result,depth,inequals):
    window=result[depth-1]+inequals[depth]+result[depth]
    return eval(window)

def bruteforce(result,depth,limit, inequals):
  if(depth>=limit):
    print('arrive')
    # print(result)
  else:
    for numchar in '123456789':
      result[depth]=numchar
      print(' '*depth,end='')
      print('given',result)
      print(' '*depth,end='')
      print('depth',depth)

      if(depth==0):
        bruteforce(result[:],depth+1,limit, inequals)
      
      result[depth]='*'
      print(' '*depth,end='')
      print('remove',result)
      print(' '*depth,end='')
      print('depth',depth)
      print('--')
      
        
      # else:
      #   token=judge(result,depth,inequals)
      #   print(token)
      #   if(token):
      #     bruteforce(result[:],depth+1,limit, inequals)
      #   else:
      #     return

#dynamic programming
def dpMarble(nums):
    # init table and items of table
    length=len(nums)
    dptable=[0]*length
    minusdptable=[0]*length

    dptable[1]=1;dptable[2]=1
    CANDs=[nums[1]+nums[3],nums[1]+nums[2],nums[2]+nums[3]]
    dptable[3]=max(CANDs)

    for i in range(5,n+1):
        #sub problems
        tokens=[]
        # 철수가 주어진 n개에 대해 1개,2개,3개 선택시 남은 갯수가 패턴상
        # 승리패턴인지 패배패턴인지 판단가능
        if(dptable[i-1]==1): tokens.append(0)
        else: tokens.append(1)        

        if(dptable[i-2]==1): tokens.append(0)
        else: tokens.append(1)

        if(dptable[i-3]==1): tokens.append(0)
        else: tokens.append(1)

        CANDs=[dptable[i-1],dptable[i-2]+nums[i],dptable[i-3]+nums[i-1]+nums[i]]
        
        dptable[idx]=max(dptable[idx-1]*nums[idx],nums[idx])
        # expansion part of kadene
        if(abs(minusdptable[idx-1]*nums[idx])>abs(nums[idx])):
            minusdptable[idx]=minusdptable[idx-1]*nums[idx]
        else:
            minusdptable[idx]=nums[idx]

        dptable[idx]=max(minusdptable[idx-1]*nums[idx],nums[idx])


        dptable[i]=max(tokens)

    return dptable[n]