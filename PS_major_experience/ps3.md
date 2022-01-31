## ps3 Implemetation experience : example || Error and Solution

#### Error and Solution 1
Error : shallow copy 및 인덱스 초기화(특히 다중 반복문 내)

파이썬의 장점이자 단점으로 정적 변수_int 등_을 제외하곤 포인터를 통해서 값이 공유됨,

즉, listA=[1,2,3,4,5]에서 listB=listA를 하면

[1,2,3,4,5]를 listA와 listB 모두가 가리킨다고 이해하면되고, listB로 원본에 접근해서 수정하면 listA에도 반영됨


Solution : 스플릿을 통해서 재할당 혹은 딥카피

listB=listA[:]

이러한 문제 연장선에서 파이썬의 장점이자

for item in items:
	print(item)
	
방식의 경우 for문이 중첩되면 원하는대로 작동안할때가 있음, 특히 중간에 인덱스를 초기화안하고 중첩 및 제어 실패해서

이런 경우를 대비해서 아에 인덱스방식으로 구현 및 for문마다 초기화하면 많은 문제 해결 예방가능


#### Error and Solution 2 : 오타 및 들여쓰기 오류
Error : = 대신 == || += 기입할려다가 =+ || 구현 초기 단계에서 넣은 매직넘버로 작동오류 || 파이썬 들여쓰기 오류

가령, for i in range(4): blabla...

4가 문제의 매직넘버

들여쓰기 오류의 경우 가령, 프로그래머스에서 코드 길어지는데, 선이 따로 안보여서 오류나기 쉬움


Solution : 중간체크 뿐, 그리고 문제풀이 많이


#### Error and Solution 3 : runtime error
Error : runtime error문, 주로 리스트나 2차원 이상 리스트의 인덱스 초과

Solution : 인덱스 범위 재설정 및 기준이 되는 minimum, maxmum, interval을 너무 작거나 너무 큰지 확인


#### Error and Solution 4 : 재귀구조에서 return을 안한 경우
Error : 재귀구조에서 return을 안한 경우

Solution : 재귀구조 간 스텝에서 return을 통해 최종 결과값까지 원하는 값을 보내도록 한다.

#### Error and Solution 5 : 'limit이 0 또는 1 인 경우에 한하여 액션한다.' 는 if(limit == 0 or 1) 이 아니다!!!
Error : 수학적 사고를 컴퓨터로 옮길때, 약간의 표현상 오차를 착각

Solution : limit == (0 or 1)