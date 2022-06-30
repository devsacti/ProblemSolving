# Problem Solving WarmUp to remind key points

## [ps1-oriented : Comprehension about Problem](./ps1)
#### 문제 반복적으로 읽어 예제 케이스와 실제가 다름을 잡자
* class president !! 예제(부분)는 5행 5열이지만, 실제(전체) 문제 조건은 n행 5열이다.

#### 수학적 지식으로 패턴 도출하기
* streetree !! (Hint GCD * LCM = a * b)

## [ps2-oriented : Applying computer algorithms](./ps2)
from computer algorithms to comprehension of problem

### Basic Computer Algorithms
* sorting and binarysearch 
* recursive extensions
* Depth First Search - Breadth First Search
* Topology Sort
* dijstra and floyd warshall
* dynamic programming
###

#### computer algorithm : sorting and binarysearch 

정렬 후 이진탐색 속 start,end의 역할, 그리고 활용 => 랜선자르기

정렬 후 이진탐색 속 while 속 조건식과 s,e(two pointer) 관계, 그리고 '언제 break하지?' => 두 용액

#### computer algorithm : recursive extensions

재귀구조와 백트래킹 => bruteforce ; recursive_series(product, permutaions,combinations,factorial), N-queens

#### computer algorithm : dynamic programming
dp => makenum, sum_rectangular

#### computer algorithm : Depth First Search - Breadth First Search

dfs-bfs => 바이러스(dfs),DFS와 BFS

dfs-bfs를 활용한 그래프 속 트리 도출 그리고 분석 => Graph to Trees and analyze

인접리스트로 구체화되지 않은 그래프에 대해 dfs-bfs 적용하기(혹은 2차원 매트릭스를 그래프로 간주하고 분석하기)  => 단지 번호 붙이기(dfs 다음 bfs), 벽 부수고 이동하기(bfs 다음 dfs)

#### computer algorithm : Topology Sort

Topology Sort(위상정렬) => 동굴탐험

###### dfs-bfs related

결과는 같더라도, 문맥상 dfs가 더 적절한 경우와 bfs가 더 적절한 경우가 존재한다고 생각, 가령 최단거리 연관 문제는 bfs쪽이 와닿거나 효과적이라고 생각 

dfs-bfs 순회과정에서 '2d matrix to graph'로 자료구조화가 가능하나 코테에 부적합

'dfs based on stack VS dfs based on recursive' => 본질은 같고 후자가 테스트에 적합

#### computer algorithm : dijstra and floyd warshall
dijstra(feat. heap) => 파티

floyd warshall => 파티

# [ps3-oriented : Implementation](./ps3)
구현 중의 기본 문법이나 쉘로우 카피, 인덱스, 초기화 설정, library 활용 등에 대해서 집중하는 단계

## Basic
#### 주어진 정보에 적합한 자료구조 적용 및 구현하기
* 숫자피라미드, class president

#### 적합한 다중 for문 적용 및 구현하기(중요)
* baseballgame

#### 2차원 matrix 접근과 활용 적용 및 구현하기
* bingo

## Extensions
Basic과 달리, ps1,ps2를 모두 아우르는 문제들,
[PS-POOL](../PS-Pool/)에서 반복학습

# Background
* [ps1](https://github.com/devsacti/ProblemSolving/blob/main/PS-Introduction/ps1.md)
* [ps2](https://github.com/devsacti/ProblemSolving/blob/main/PS-Introduction/ps2.md)
* [ps3](https://github.com/devsacti/ProblemSolving/blob/main/PS-Introduction/ps3.md)
