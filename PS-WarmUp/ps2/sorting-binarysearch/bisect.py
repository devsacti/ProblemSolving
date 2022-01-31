# step 3 implementation
from bisect import bisect_left,bisect_right

if __name__=="__main__":
  n,q=map(int,input().split())
  
  nums=list(map(int,input().split()))
  nums.sort()
  # print([0,1,2,3,4,5,6,7,8,9])
  # print(nums)
  quests=list(map(int,input().split()))
  
  for quest in quests:
    l_i=bisect_left(nums,quest)
    r_i=bisect_right(nums,quest)
    # print(l_i)
    # print(r_i)
    # print('--')
    print(r_i-l_i)
  