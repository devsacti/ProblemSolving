## ps2 Applying computer algorithms to Comprehension experience : example || Error and Solution
Error and Solution에서 Solution는 대체로 아래와 같은 중간 체크 습관이 유일한 답이고 그 다음 많은 문제풀이가 답이다.

Sol0) 사후 print는 기본 check용 print format 만들기

print

 for, while, func1 

  print

  print

print


Sol1) 해도 안되면, 뜸들이지 말고 다시처음부터 짜라. 시간이 부족해도 최선

### ps2.1 utilizing and modularizing computer algorithms

#### example1 2차원 좌표로 표현된 속이 빈 치즈의 단면에서 치즈안팍,즉 In-out을 구분하라
=> 방문좌표에서 dfs찍었을때, 좌표범위를 넘으면 OUT, 아니고 원만히 치즈라는 벽을 넘지 못하고 다 순회하면 IN 

#### Error and Solution 1 
Error : 2개 이상 시 체크 != 2개가 되면 체크

Solution : 우선 print로 중간체크하는 습관, 그리고 많이 풀기

##### explaination

L10_08, cnt가 2개 이상이면 체크 => 2개가 되면 1번 체크해야되는데 2개가 된 케이스가 3개 4개가 될때마다 과다 체크

사람이었다면, 아까 체크한거자나! 이러면서 넘겼겠지만, 컴퓨터는 아니다! 이와같은 걸 기대할려면 또 변수선언필요

숫자를 1개씩 가져와서 입력받는 상황에서, 즉 과정중 관찰 및 처리

숫자별 빈도수를 저장하는 test list에 2개, 3개, 4개 등 '2개 이상' 중복된 숫자가 있다면

부적합 판정을 내려야하는 상황이다.

나는 여기서 '2개 이상', 중복'이란 키워드 속에서 아래와 같이 코드를 연상했다. 

                    if(test_list[seqs[i]-1]>=2):
                        cnt_2+=1

그러나 이는 결과에 대한 관찰 및 처리 코드와 과정중 코드가 섞인 불순코드이다.

                    if(test_list[seqs[i]-1]==2):
                        cnt_2+=1

애당초 1개씩 입력받는 과정에서는 전체코드가 갱신되는 과정이라 

현재 들어온 숫자와 그 숫자의 test_list 속 빈도수가 계속 갱신되는 과정이라

저렇게 결과에 대한 if문을 적용하면 에러가 생긴다.

가령, 1 1 3과 같이 1이 연달아서 들어왔다가 다른 숫자가 나오면 상관없다.

근데 만약 1 1 1 5 이라면 1의 빈도 수는 3개이고 5의 갯수는 1개이고, 중복된 발생 횟수는 2번이나,

위 코드는 3번을 카운팅한다, 1 1-> cnt_2 1증가, 후 1들어오면 cnt_2 또 1증가

한편, testlist가 완전히 갱신된다음이라면

for element in ~:
    if(element>=2)꼴도 맞긴하다.

#### Error and Solution 2 
Error : (i+1)%10 는 (i%10)+1 와 다른데, 착오!

Solution : 우선 print로 중간체크하는 습관, 그리고 많이 풀기

### ps2.2 Integration of modules with Time Complexity

### ps2.3🥇 humble approach to hidden hidden case

#### example1 추가적인 테스트 케이스 추가
당최 어떤 케이스에서 불충족인지 감이 안올때는 운에 맞기도 케이스 대입해야

L6_08문제에서 왠지 모르게 80점 나옴, 그냥 ABBCCCDDDDCCCBBA대입해보니,

마지막이 ABBCCCDDDDCCCBBB라면 생기지 않을 문제가

마지막에 반복이 끝날때 생기는 문제를 발견함.

[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (3, 'C'), (2, 'B'), (1, 'B')]

A2B3C4D3C2BB
