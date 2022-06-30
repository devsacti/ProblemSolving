'''
ps1.2.
가장 생각하기 쉬운 abababab에서 abababac인 경우를 처리하고, 그렇게 확장하면 패턴잡기 쉬울듯

ps2. applying computer algorithm
이중 for문 => 자르는 단위별 압축

ps3.
시작점을 꼭 0부터 할려고하기보단 prev설정을 통한 유연함
'''

def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s)//2 +1):
        compressed=""
        std=s[0:unit]
        count=1
        
        for idx_cur in range(unit,len(s),unit):
            
            if std == s[idx_cur:idx_cur+unit]:
                count+=1
            
            else:
                if count>=2:
                    compressed += str(count)+std
                else:
                    compressed+= std
                    
                std = s[idx_cur:idx_cur+unit]
                count=1
        
        if count>=2:
            compressed+= str(count)+std
        else:
            compressed+= std
            
        answer=min(answer,len(compressed))

    return answer