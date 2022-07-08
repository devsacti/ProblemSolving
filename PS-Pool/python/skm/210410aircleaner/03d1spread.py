import sys

'''
summary;
1. 값 갱신할때, 새로 변수 선언해야 이전 시행의 영향 방지
2. 최적화>>범용성

-----
1을 기준으로 생각하기보다
여집합의 관점에서 현재 노드가 0이면 그 주변에 1이 있는지 보고
전환하는 게 구현관점에서 
!! 안좋다!

왜냐하면 확산받은 0이 1이 되고 그 옆 0도 또 확산된 1 보고 확산되면 다 1됨
1을 기준으로 생각하자
=> 1을 기준으로 생각해도, 따로 결과 반영할 seq 변수 생성안하면 같은 문제 생김

! 중요한 건 이전 시행이 다음 시행에 영향을 못가게, 새로 변수 선언
그렇게 하면 0을 기준으로 하든 1을 기준으로하든 무관

+
주어진건 1차원인데, 구태여 2차원 환경을 확장해서 코드짤라니까

특히 좌표이동 관련해서 2차원을 염두한 설계를 
1차원 환경에 적용할때 너무 말린다.

반복학습할때, 확장하고 지금은 그저 가장 빠른 길을 찾자
'''

# def spread_robot():
#     global N,seq

#     mag=1
#     dc=[mag,-mag]

#     kinds_vectors=len(dc)

#     for d in range(kinds_vectors):


if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    seq=list(map(int, sys.stdin.readline().split()))
    result_seq=[0]*N

    # print(N,seq)

    for idx_val, val in enumerate(seq):
        if(val == 1):
            result_seq[idx_val]=val

            # tmp_~ : index
            tmp_left=idx_val-1
            tmp_right=idx_val+1

            if(tmp_left<0):
                pass
            else:
                result_seq[tmp_left]=1

            if(tmp_right>N-1):
                pass
            else:
                result_seq[tmp_right]=1

    print(' '.join(map(str,result_seq)))
