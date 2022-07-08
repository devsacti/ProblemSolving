# y ,x max가 그리 크지 않으니, 그냥 최대 매트릭스 선언해두고 풀자
# 아니라면 사전 썼을듯
import sys

coordinates={}

if __name__=="__main__":
    n = int( sys.stdin.readline().strip() )
    r, c = 110,110

    matrix=[[0]*c for _ in range(r)]

    duplications=[]
    for _ in range(n):
        r,c = map(int, sys.stdin.readline().split())
        matrix[r][c] +=1
        if(matrix[r][c]==2):
            duplications.append( (r,c) )
    
    for dup in duplications:
        n -= matrix[dup[0]][dup[1]]

    print(n)