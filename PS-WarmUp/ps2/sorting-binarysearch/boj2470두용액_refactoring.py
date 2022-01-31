'''
* 앞선 주석은 최초파일과 동일


확장형 이진 탐색 방식 ; 꼭 1개를 추출하는 것이 아니라 애당초 단위를 2~3개로 확장해서 추출
시간 초과 문제 해소,

애당초 2~3개씩 뽑는다.

그리고 이전에는 특징값의 정의에 따라_abs(A+B)_패턴을 찾았고
그 패턴이 이차함수에 대한 분석이었지만, 시간초과가 발생
=> 보다 비교연산 등을 줄일 수 있는 패턴정의 필요.

'''

def bs(sorted_seq,n,std):

    # index of left-right pointer : s-e
    s=0
    e=(n-1)
    
    # s+0<=e 조건을 반복하다 정지 직전 상황에서는, 추출 구간의 길이가 1이되고, 정지 후에는 e-s의 값이 -1이 된다고 할수있다.
    # s+1<=e 조건을 반복하다 정지 직전 상황에서는, 추출 구간의 길이가 2이되고, 정지 후에는 e-s의 값이 0이 된다고 할수있다.
    # s+2<=e 조건을 반복하다 정지 직전의 상황에서, 추출 구간의 길이는 3이 되고, 정지 후는 e-s의 값이 1가 된다.
    
    # 한편,
    # 3으로 상정한 순간, 즉 s와 e사이에 최종적으로 1칸이상이 존재하길 기대한다면,
    # s와 e를 mid를 기반으로 업데이트할때, +-1을 하지 않는다.
    # 왜냐하면 이것의 목적은 mid 산출 시 나눗셈한 idx값이 시 더이상 정지후 e-s의 값이 -1이 되지 않는 상황에 대응하기 위한 처리이기 때문이다.

    # 왜냐하면
    # bs의 메카니즘은 while의 조건과 mid의 업데이트 2요소인데, 
    # 구간이 1일때, s가 (e-1)일때 발생하는 무한루프가 발생하지 않아서
    # 1요소만 사용한다고 이해가능
    while(s+2<=e):
        idx_mid=(s+e)//2
        
        if(std+sorted_seq[idx_mid]==0):
            # idx_mid가 ideal idx인 경우, 현재 idx가 perfect pair의 idx인 경우, 기준값과 그 음수를 리턴
            
            # !! 사실상 break인 지점이다
            return (std, -std)
        elif(std+sorted_seq[idx_mid]<0):
            # 정렬된 이상 뒤로갈수록 크다
            # 그리고, 위와같은 'ideal idx의 val와 비교할때'
            # 그리고, 앞에서 '양수로만', 혹은 '음수로만' 구성된 케이스를 처리했기에
            # 상단의 합의 함수는 ideal idx일때 0이고, 증가하는 일차함수꼴이 된다.
            # 합이 0보다 작다는 것은 더 큰 값들의 구간을 살펴야 ideal을 찾을수있다는 의미이다.
            s=idx_mid
        elif(std+sorted_seq[idx_mid]>0):
            e=idx_mid
        else:
            pass

    # std는 별도이고, 2칸짜리 추출구간이 있다고 이해하면된다.
    # 그리고 이 2칸에 대해 std는 2쌍을 생성할수있다.
    candi1_pair=(std, sorted_seq[s])
    candi2_pair=(std, sorted_seq[e])

    # 자기 자신과 맵핑된 중복쌍의 경우를 처리한다.
    if( candi1_pair[0]==candi1_pair[1]):
        # 첫번째 쌍이 중복쌍인 경우, 그렇지 않은 것을 리턴
        return candi2_pair
    elif( candi2_pair[0]==candi2_pair[1]):
        # 두번째 쌍이 중복쌍인 경우, 그렇지 않은 것을 리턴
        return candi1_pair
    else:
        val_candi1=abs(sum(candi1_pair))
        val_candi2=abs(sum(candi2_pair))

        if(val_candi1<val_candi2):
            return candi1_pair
        else:
            return candi2_pair  


if __name__=='__main__':
    n=int(input())
    seq=list(map(int, input().split()))

    sorted_seq=sorted(seq)
    # print(sorted_seq)

    list_candidates=list()
    token_approximate=1

    # 정렬 후 리스트의 최소값이 양수인 경우, 혹은 최대값이 음수인 경우에 대해선 
    # 답이 정해지므로 아래와 같이 처리하는데,
    # 이를 통해서 else의 경우 언제나 음수와 양수의 조합으로만 된 경우를 상대할수있다!!
    # => bs의 비교연산부분이 더욱 간단해진다.
    if(sorted_seq[0]>=1):
        print(sorted_seq[0], sorted_seq[1])
    elif(sorted_seq[-1]<=-1):
        print(sorted_seq[-2], sorted_seq[-1])
    else:
        # min_sum_feature=100
        min_sum_feature=int(1e20)
        answer=(0,0)

        for std in sorted_seq:
            result=bs(sorted_seq,n,std)

            if(abs(sum(result))<abs(min_sum_feature)):
                min_sum_feature=abs(sum(result))
                # 문제요구 조건 상 같은 특징값을 가진 쌍을 모두 찾는 것이 아니기에 =은 제외
                answer=result

        print(answer[0],answer[1])