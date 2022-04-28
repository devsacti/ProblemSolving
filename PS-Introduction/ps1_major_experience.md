## ps1 Comprehension about Problem experience : example || Error and Solution

### ps1.1 Analsis == 문제 눈으로 선그으면서 읽고, 개별 조건에 대한 명시적 이해

#### Error and Solution1 : misreading => drawing a line by eye again and again....

as-is : print('No')

to-be : print('NO')

#### Error and Solution2 : example misunderstanding => imagine another example aside from given
!! 예제의 함정 : 주어진 예제에만 맞춰서 나도 모르게 전체 패턴을 놓침 !!

우선 주어진 예제말고 다른 것도 스스로 생각한다. 그리고 문제를 많이 푼다.

가령1,

L3 class President에서 주어진 예제는 5행 5열이나 실제론 n행 5열이다.

이를 곡해하여 로직을 5라는 매직넘버에 맞춰서 짤경우, 나머지 케이스가 모두 에러된다.

가령2,

L3 maxofarr 문제에서

예제에는 최댓값이 2개까지인 경우만 소개되어있고, 나도 모르게 max(a,b)와 같이 2개를 상정한 알고리즘으로 구현함 => 오차발생

반드시 주어진 예제 외에도 추가로 만들어보자,최대한

### ps1.2 drawing pattern,exceptions == 패턴 찾기와 예외처리

#### example 1
가령, 주어진 조건들이 아래와 같고 특정 인덱스의 값을 리턴을 요구 할 때,
 
Condition1 : 주어진 1번째항과 2번째 항의 범위는 정수(+주어진 예제는 모두 자연수)

Condition2 : 3번째는 1번째,2번째의 합으로 정의,,,,n번째는 n-1과 n-2번째의 합으로 정의

=> 피보나치 수열 이론과 dp 접목하여 이해하기

만약 추가로 

Condition3 : 증가하는 수열에 한해서만 출력값 요구

Condition1으로 인해 최초항이 -1,-2 인 경우를 고려했을지라도,

-1,-2가 1,2번째항으로 주워지면 이 피보나치 규칙에 기반한 후속값들은 점점 작은 음수값이 되므로 예외처리해야 한다.

#### Error and Solution 1 : finding mispattern => solving many problems and record
121

1213121

121312141213121

1213121412131215121312141213121

try1_1213121 단위로 분할 => 4 5 4란는 약간의 규칙성이 보이나 부족

1213121 4 1213121 5 1213121 4 1213121

try2_인덱스_또는 depth_와 이전 값과의 연관성에서 패턴 도출 => 모두 설명 가능

(이전 문자열)+"(현재 인덱스+2)"+(이전 문자열)

#### 문제 이해 관련 주요 방식,이론, 개념들
일단 정렬해보기!!!

[점화식](https://m.blog.naver.com/PostView.nhn?blogId=freewheel3&logNo=220846174457&proxyReferer=https:%2F%2Fwww.google.com%2F),

피보나치,

소수개념과 에라토스테네스의 체 등등
