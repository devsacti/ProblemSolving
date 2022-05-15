# sorting with priority and bisect
e2 = sorted(a, key = lambda person : (person[0],person[2], -person[1]))
## 다중 정렬은 어떻게 구현할까? 
## 내 예상
## (1, 4, 1)
## (2, 3, 3)
## (2, 2, 3)
## (4, 1, 4)

# dictionary sort
d1 = sorted(d.items())
d1 = sorted(d.items(), reverse=True)

d2 = sorted(d.items(), key=lambda x: x[1])
d2 = sorted(d.items(), key=lambda x: x[1], reverse=True)

# 출처: https://blockdmask.tistory.com/566 [개발자 지망생]

##  우선 각 인스턴스의 0번째값으로만 인덱스 정렬, 그 다음 

from bisect import bisect_left
from bisect import bisect_right

# caution bisect_left right can output 'out of index' cuz this purpose is 'insert'
# nums  [1, 1, 2, 2, 4, 4, 4, 7, 7, 10]

# if print(bisect_left(nums,4)) and print(bisect_right(nums,4))
# index  0  1  2  3  4  5  6  7  8   9
#                    |                 => result is 4
#                             |           => result is 7
# left means that " 3 canbe inserted at 4 "
# right means that " 3 canbe inserted at 7 "
# insert 기준이라 반드시 left의 경우 반환된 인덱스와 그 좌우를 출력해봐야함
# 가령, bisect_left(nums,3)이면 없다가 아니라, 똑같이 인덱스 4를 출력함 그리고 3이 좌우에 없는경우도 살펴야함

# so if 11 was given left and right result is 10 which is out of range

# 출처: https://programming119.tistory.com/196 [개발자 아저씨들 힘을모아]
## and remind parameter binary search by custom function

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