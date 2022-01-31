'''
reference : 알고리즘잡스 L10
sub reference(unstable) : https://dobbury.tistory.com/173

ps1. comprehension about problem
ps1.1. analysis

번째 => 1 부터 시작

K는 N*N보다 작거나 같고, 10,000,000,000보다 작거나 같은 자연수이다. 
=> binary search

ps1.2. drawing pattern, exceptions

pattern1.
k를 기입하면 원하는 숫자를 산출하는 함수_k(order) => number_가 있다고 가정하자, 그러나 이는 정렬을 필수적으로 요구하므로 시간복잡도가 매우크다.
=> 그렇다면 이러한 정렬을 피할 수 있는 다른 접근방식, 혹은 다른 독립변수를 찾자
=> 우리가 원하는 함수의 우선 '역함수_number => order_'로 접근을 해보자


ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing computer algorithms

module 1 ; binary search
start is 1, end is N*N, and binary

!! 다만 컴퓨터 알고리즘 상 오차가 발생한다. 즉, 테이블의 실제 값들에는 중복값이 있으나, 당장 구현가능한 후보값들은 이런 패턴이 없다.
가령, 5 * 5 table을 기준으로 설명하자면,
내가 구현 가능한 샘플 스페이스는 1 ~ 25이다.
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ; executable samplespace

하지만 실제 테이블에는 중복으로 인해 샘플스페이스가 더 적다.
1 2 3 4 5
  2   4   6   8   10
    3     6     9       12       15
      4       8         12          16          20          
        5         10             15             20             25
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
1 2 3 4 5 6   8 9 10    12       15 16          20             25 ; items from NN table

from NN table, which N is 5
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25

하지만, 여전히 정방향 접근은 시간복잡도 상 불가능하다.
현실 속 패턴을 살펴보고, 현재 구현가능한 ideal 방식의 오차를 수정하는 방식으로 문제를 풀어간다.

(real)
1  2  3  4  5  6     8  9  10      12          15  16              20                  25 ; real items from NN table
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
0  1  3  5  8  10    12 14 15      17          19  21              22                  24 ; cnt of front items 'based on NN table'
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
1  2  2  3  2  2     2  1  2       2           2   1               2                   1  ; itself_count 1,2,3 ; 제곱수는 자기자신과 같은 값이 1 또는 3개, 아닌것은 대칭형태로 2개
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
1  2  4  6  9  11    13    16      18          20                  23                   
   ~  ~  ~  ~  ~     ~     ~       ~           ~                   ~                  
   3  5  8  10 12    14 15 17      19          21  22              24                  25 ; order range 'based on NN table'_ex) 1, 2~3, 4~5, ....
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 

(ideal)
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 ; executable samplespace
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
1  2  3  4  5  6  7                                                                  ..25 ; useless 'transfering value to order' based on samplespace
- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 

!! (Real)의 'cnt of front items'를 구현해보려고 시도해보자 => 어렵다...자기자신 갯수때문에
=> 자기자신의 갯수를 포함한 순서를 구해보자

가령, 12는 자기자신 포함 앞에는 몇개가 있을까?
1의 배수는 5개, 2의 배수는 5, 3의 배수 4개, 4의 배수 3개, 5의 배수 2개, 19

=> module 1.1
    cntMultiples_perRow=[int(mid//(i)) for i in range(1,root_end+1)]
    cntMultiples_perRow=[root_end if cnt>root_end else cnt for cnt in cntMultiples_perRow]

- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
1  3  5  8  10 12    14 15 17   17 19  19  19  21  22              24                  25 ; order range 'based on NN table'_ex) 1, 2~3, 4~5, ....
                                  | 
                                threshold

만약 k가 19이면 samplespace 상으론, 12,13,14 모두 성립하나, 실제 nn테이블상에선 12만 존재한다.
즉, mid가 13,14더라도 이진탐색을 계속해서 12가 되도록 설정해야한다.

우선 이를 위해 break을 하지 않고,
최초로 19보다 작아지는 11에 근사하게 다가가되, 최종적으로 길이가 구간의 길이가 2일때 작으면 s를 증가시켜 결국 11 다음 12에서 이진탐색을 멈추게한다.

k가 18일때도 동일하게 작동한다. '바닥을 이용하면서' 동시에 18~19번째가 모두 동일한 중복값인 것을 이용하는것이다.

매우매우 어렵다. 어떻게 보면 오차를 감수했지만, 자료특성상 상관이없었던 케이스로도 이해가능하다

한편, 이진탐색이란 건 '대표값을 바탕으로 구간을 구체화해가능 과정'으로 이해할수있지 않을까

ps2.2. integration

ps3. Impl
'''

import sys

# module 1
def bs(start, root_end,k):
    # s,e NOT INDEX OF COMPUTER
    s=start
    e=root_end*root_end

    while(s<=e):
        # print('start~end',s,e)
        mid=int( (s+e)/2 )
        # or mid = (s+e)//2
        # print('#mid',mid)
        
        # module 1.1
        cntMultiples_perRow=[int(mid//(i)) for i in range(1,root_end+1)]
        cntMultiples_perRow=[root_end if cnt>root_end else cnt for cnt in cntMultiples_perRow]
        order_Mid=sum(cntMultiples_perRow)
        # print('order_Mid',order_Mid)

        if(order_Mid>=k):
            result=mid
            e=mid-1
            # DO NOT BREAK!
            # cuz, 1~25 is not fit with real component of table
        elif(order_Mid<k):
            #result=order_Mid를 할수는 있는데 그러면 추가적으로 처리 요구
            s=mid+1

    print(result)
    # result2=checkintable(result,root_end)
    # print(result2)

if __name__=='__main__':
    N=int(sys.stdin.readlin().strip())
    K=int(sys.stdin.readlin().strip())

    bs(1,N,K)
