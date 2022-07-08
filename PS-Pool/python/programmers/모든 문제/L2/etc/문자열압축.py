'''
https://programmers.co.kr/learn/courses/30/lessons/60057

ps1.2.
가장 생각하기 쉬운 abababab에서 abababac인 경우를 처리하고, 그렇게 확장하면 패턴잡기 쉬울듯

ps2. applying computer algorithm
이중 for문 => 자르는 단위별 압축

ps3.
시작점을 꼭 0부터 할려고하기보단 prev설정을 통한 유연함
'''

def solution(s):
    answer = len(s)

    # 1개 단위(unit_compress)부터 압축 단위를 늘려가며 확인
    for unit_compress in range(1, len(s) // 2 + 1):
        compressed = ""
        # 최초의 prev이자 std, 추후 다른 sub문자열 출현 시 변경된다
        prev = s[0:unit_compress]  # 앞에서부터 unit_compress 문자열 추출
        count = 1
    
        # 단위(unit_compress) 크기만큼 증가시키며 이전 문자열과 비교
        for idx_cur in range(unit_compress, len(s), unit_compress):
        
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[idx_cur:idx_cur + unit_compress]:
                count += 1
            
            # 다른 문자열이 나왔다면, 문자열을 압축해서 저장하고, 새로운 prev설정 후 지속
            else:
                if count>=2:
                    compressed += str(count) + prev
                else:
                    compressed += prev

                prev = s[idx_cur:idx_cur + unit_compress]  # 다시 초기화
                count = 1
            
        # 중간에 다른 패턴을 만나지 않아 한번도 압축되지 않은 경우나, abababab => 4ab
        # 어느 기점부터 계속 같아서 한번도 압축되지 않아 남아 있는 문자열에 대해서 처리
        if count>=2:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        # 만들어지는 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer