# y ,x max가 그리 크지 않으니, 그냥 최대 매트릭스 선언해두고 풀자
# 그냥 좌표마다 최소값 갱신 후에 유효좌표로 방문하는 거나
# 사전형태로위치별 최소값 갱신하면서 value만 합치거나, 일단 후자 더 빠를거같아서
import sys

coordinates={}

if __name__=="__main__":
    n = int( sys.stdin.readline().strip() )
    r, c = 110,110

    # matrix=[[0]*c for _ in range(r)]

    num_Human=1
    duplications=[]
    for _ in range(n):
        # num_Human
        r,c = map(int, sys.stdin.readline().split())
        
        if( (r,c) not in coordinates.keys() ):
            coordinates[(r,c)]=num_Human
        else:
            # 인풋특성 상 1번부터 n번 순이라 나중에 들어온 num은 언제나
            # 현재 키 값을 하는 num보다 크다, 좌표별 누적수면 모를까 갱신필요x
            pass
        num_Human += 1 
    

    print(sum(coordinates.values()))