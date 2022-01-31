'''


step1 understand and write, input

이미 심어져 있는 가로수의 수=정수 N
3≤N≤100,000

N개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수
가로수의 위치를 나타내는 정수는 1,000,000,000 이하
가로수의 위치를 나타내는 정수는 모두 다르며
가까운 위치에 있는 가로수부터 


4
//
1
3
7
13


step2 최소간격을 찾자, 길이를 찾자, 찾은 값에 따라 업데이트보단 새로운 리스트를 선언하자.

코치님 설명; 간격들 간의 최대공약수를 사용하라



def findmininterval(line):
    count_check=len(line)-1

    interval=[]

    for i in range(count_check):
        interval.append(line[i+1]-line[i])

    return interval

if __name__=='__main__':
    N=int(input())

    line=[]

    for i in range(N):
        line.append(int(input()))

    origin=line[:]

    interval_line=findmininterval(line)
    min_interval_origin=min(interval_line)

    ideal_line=[i for i in range(line[0],line[-1]+1,min_interval_origin)]

    for element in line:
        if (element not in ideal_line):
            ideal_line.append(element)
    
    post_line=sorted(ideal_line)
    interval_line=findmininterval(post_line)
    min_interval_post=min(interval_line)

    # print(line, post_line)

    # breakcnt=0
    # print(line)
    while(min_interval_origin!=min_interval_post):
        # print(min_interval_origin,min_interval_post)
        # if( breakcnt==8): break

        line=[i for i in post_line]
        print(line)
        interval_line=findmininterval(line)
        min_interval_origin=min(interval_line)

        ideal_line=[i for i in range(line[0],line[-1]+1,min_interval_origin)]
        #print(ideal_line)

        post_line=[]
        for element in line:
            if (element not in ideal_line):
                ideal_line.append(element)
        
        post_line=sorted(ideal_line)
        print('post ',post_line)
        interval_post=findmininterval(post_line)
        min_interval_post=min(interval_post)

        # breakcnt+=1


    print(len(post_line)-len(origin))
'''
## template
from math import gcd

if __name__=="__main__":
  N=int(input())
  
  position_1dvectors=[]
  for _ in range(N):
    position_1dvectors.append(int(input()))
    
  # print(position_1dvectors)
  
  distances=[]
  
  #distance 
  idx=0
  while(idx+1<N):
    start=position_1dvectors[idx]
    end=position_1dvectors[idx+1]
    distances.append(end-start)
    idx+=1
  
  # print(distances)
  #finding total gcd
  #gcd argument requires 2 arguments
  idx=1
  totalgcd=0
  len_distances=len(distances)
  while(idx<=(len_distances-1)):
    # print(totalgcd)
    if(idx==1):
      start=distances[idx-1]
      end=distances[idx]
      totalgcd=gcd(start,end)
      # print(totalgcd)
      idx+=1
    else:
      next=distances[idx]
      totalgcd=gcd(totalgcd,next)
      idx+=1
  
  # print(totalgcd)
  
  totalcnt_tree=1+(position_1dvectors[-1]-position_1dvectors[0])//totalgcd
  addtionaltree=totalcnt_tree-N
  print(addtionaltree)







