# 전장속으로 A
# PS
# comprehension
# c1. 1 base indexing & 동일한 최소값은 매트릭스상 좌상 우선 => u1

# utils
# u1. 맨아래 로우부터, 그리고 오른쪽에서 왼쪽으로 탐색해서 최소값의 좌표를 갱신 / 출력 시 인덱스 1 플러스

# implement

if __name__=="__main__":
    n = int(input())

    matrix=[]

    for _ in range(n):
        matrix.append(list(map(int,input().split())))

    # print(*matrix, sep='\n')

    minimum=100000
    coord_min=[-1,-1]
    for r in range(n-1,-1,-1):
        for c in range(n-1,-1,-1):
            # print(r,c)
            if(matrix[r][c]!=0 and matrix[r][c]<=minimum):
                minimum=matrix[r][c]
                coord_min=[r,c]

    r,c=coord_min
    print(r+1,c+1)