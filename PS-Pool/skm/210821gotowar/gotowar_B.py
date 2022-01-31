# 전장속으로 B
# PS
# comprehension
# c1. A의 조건을 계승한다 => u1
# c2. 목표별 접근 소요시간을 기입한다, 자기자신은 *

# utils
# u1. 맨아래 로우부터, 그리고 오른쪽에서 왼쪽으로 탐색해서 최소값의 좌표를 갱신 / 출력 시 인덱스 1 플러스
# u2. matrix2 2d

# implement
stdR,stdC=-1,-1

def getcost(destR,destC):
    return abs(destR-stdR)+abs(destC-stdC)

if __name__=="__main__":
    n = int(input())

    # war_map ; 2d matrix
    war_map=[]
    for _ in range(n):
        war_map.append(list(map(int,input().split())))
    # print(*war_matrix, sep='\n')

    for r in range(n):
        for c in range(n):
            if(war_map[r][c]==9):
                stdR,stdC=r,c

    # info_map ; 2d matrix
    info_map=[[0]*n for _ in range(n)]

    for r in range(n-1,-1,-1):
        for c in range(n-1,-1,-1):
            # print(r,c)
            if(war_map[r][c]!=0):
                if(1<=war_map[r][c]<=8):
                    info_map[r][c]=getcost(r,c)
                elif(war_map[r][c]==9):
                    info_map[r][c]='*'

    # print(*info_map,sep='\n')

    for row in info_map:
        print(' '.join(map(str,row)))