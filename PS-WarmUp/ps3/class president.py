'''
reference : 알고리즘잡스 L3
sub reference(unstable) : https://kosaf04pyh.tistory.com/55

ps1. comprehension about problem
ps 1.
5년간 반이 같았던 지인 수가 제일 많은 학생 찾기
넘버링은 1번부터

!! input : 예제는 5*5까지 지만 정확히는 n*5이다
output :  학생 번호

ps 1.2
process for pattern : (중복 카운팅을 피하기 위해) 1번 학생과 나머지, 그리고 2번 학생은 1번을 제외한 나머지, 3번은 1,2번을 제외한 나머지와 순차 비교
!! exception : 만약 지인수가 동일한 경우, 학생번호는 제일 작은 걸로

ps2. utilizations and integrations of algorithmns for comprehension
Module 1 : 첫번째 폴문의 현재 인덱스를 활용하는 이중 for문, 되도록 1번부터 시작

알고리즘 에러1 : 나는 단순히 1~5년 간의 기록을 비교해서 같으면 지인수를 +1했는데, 1학년때 같은반이었던 애가 2학년때도 같은반으로 만났을때 지인수가 2중복 투표되는것을 발견 
=> 단순 비교 for문 수정

ps3. Impl
'''

if __name__=="__main__":
    n=int(input())
  
    records=[]
    # 넘버링 일치를 위한 append
    records.append(['*','*','*','*','*'])
  
    for _ in range(n):
        row=['*']+list(map(int, input().split()))
    
        records.append(row)
    
    # print(*records, sep="\n")
  
    # for 1 base numbering
    cnt_acquaintance={k:0 for k in range(1,n+1)}
    # 지인 수 중복 카운팅 방지를 위한 학생별 지인 list
    li_acquaintance={k:list() for k in range(1,n+1)}
    
    for cur_idx in range(1,n+1):
        std_student=records[cur_idx]
    
        for target_idx in range(cur_idx+1,n+1):
          target_student=records[target_idx]
      
          # std와 target의 5년간 반 기록 비비교
      
          for i in range(1,5+1):
              if(std_student[i]==target_student[i]):
          
                  # 중복을 피하도록 target_idx를 현재 인덱스 초과부터 잡았으므로, 일치한 2개 모두 지인수 증가
                  # => 사람 간 비교 중복은 피했으나, 다른 학년에서 만났을때의 지인카운팅 중복은 못피함
                  if(target_idx not in li_acquaintance[cur_idx]):
                      li_acquaintance[cur_idx].append(target_idx)
                      cnt_acquaintance[cur_idx]+=1
                      cnt_acquaintance[target_idx]+=1
                  
          # print(cur_idx, cnt_acquaintance)
          
    # print(cnt_acquaintance)
    
    # 초기값은 되도록 답으로 설정한다, 만약 서로 모두 지인이 없는 경우, 1번학생이 0이다.
    max_cnt=0
    answer=1
    for k,v in cnt_acquaintance.items():
        # print(k,v, max_cnt)
        # 지인 수가 초과한 경우에만 갱신하므로서 최초의 최대 지인수를 가진 학생번호가 유지
        if(v>max_cnt):
            # print('ck')
            max_cnt=v
            answer=k
            # print('##',answer)
            
    print(answer)
    