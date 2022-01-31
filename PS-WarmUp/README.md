# Problem Solving WarmUp to remind key points
* 개인적으로 실제 코테에서는 3 1 2 again 3의 순환을 거치므로, 이와같은 순서를 우선하기 희망

# ps1-oriented practice or record [goto](https://github.com/devsacti/Algorithms-ProblemSolving/tree/main/ProblemSolving/PS-WarmUp/ps1)
## 예제 케이스에 속지 마라
class president !! 예제(부분)는 5행 5열이지만, 실제(전체) 문제 조건은 n행 5열이다.

## 수학적 지식으로 패턴 도출하기
streetree !! (주석 처리는 아직)

# ps2-oriented practice or record [goto](https://github.com/devsacti/Algorithms-ProblemSolving/tree/main/ProblemSolving/PS-WarmUp/ps2)
from computer algorithms to comprehension of problem

## sorting and binarysearch 

정렬 후 이진탐색 속 start,end의 역할
=> 랜선자르기

정렬 후 이진탐색 속 while 속 조건식과 s,e(two pointer) 관계, 그리고 '언제 break하지?'
=> 두 용액

정렬 후 이진탐색 속 if의 커스텀과 break의 역할(패턴 도출도 어렵다; 역함수)
=> NN단표

## recursive extensions

재귀구조와 백트래킹
=> bruteforce ; recursive_series(product, permutaions,combinations,factorial), N-queens

## Depth First Search - Breadth First Search

dfs-bfs
=> 바이러스(dfs),DFS와 BFS 

+ 'dfs based on stack VS dfs based on recursive(본질은 같다!)'

dfs-bfs를 활용한 그래프 속 트리 도출 그리고 분석
=> Graph to Trees and analyze

인접리스트로 구체화되지 않은 그래프에 대해 dfs-bfs 적용하기(혹은 2차원 매트릭스를 그래프로 간주하고 분석하기) 
=> 단지 번호 붙이기(dfs 다음 bfs), 벽 부수고 이동하기(bfs 다음 dfs)
* 결과는 같더라도, 문맥상 dfs가 더 적절한 경우와 bfs가 더 적절한 경우가 존재한다고 생각, 특히 최단거리는 bfs쪽이 와닿거나 효과적이라고 생각

* 참고로 dfs-bfs 순회과정에서 '2d matrix to graph'로 자료구조화가 가능하나 코테에 부적합

+a 위상정렬(주석은 아직)

## dijstra and floyd warshall
dijstra(feat. heap)
=> 파티

floyd warshall
=> 파티

## dynamic programming
makenum
(주석 정리는 아직)

sum_rectangular
(주석 정리는 아직)

# ps3-oriented practice or record [goto](https://github.com/devsacti/Algorithms-ProblemSolving/tree/main/ProblemSolving/PS-WarmUp/ps3)
* 이론적인 ps2 과정을 실행하는 단계로서, 구현 중의 기본 문법이나 쉘로우 카피, 인덱스, 초기화 설정 등에 대해서 집중하는 단계

숫자피라미드 !! 주어진 정보에 적합한 자료구조 구현

class president !! 주어진 정보에 적합한 자료구조 구현

baseballgame !! 문제 해석에 따른 다중 for 문 구현

bingo !! 2차원에 대한 가로,세로,대각선 접근방식 구현

## effective and useful implementation records [goto](https://github.com/devsacti/Algorithms-ProblemSolving/tree/main/ProblemSolving/PS-WarmUp/Useful_Impl_Records)

handlingMatrix

how to describe the vector in 2d


