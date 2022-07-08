# 조회 알고리즘2
# 오전 11:08 2021-04-22
# 사전형태로위치별 최대값 갱신하면서 value만 합치기
import sys

# summary of condition
# At init, n people are there, and human has y,x,age
# during t, per second, k people get in with same information.
# per coordinate, max age object is remain the other is removed

# summary of algorith
# per coordinate, which implemented by dictionary, only max value is updated

coordinates={}

if __name__=="__main__":
    n,k,t = map(int, sys.stdin.readline().split() )

    for _ in range(n):
        # y, x ;NOT INDEX OF COMPUTER
        y,x,age = map(int, sys.stdin.readline().split())
        
        if( (y,x) not in coordinates.keys() ):
            coordinates[(y,x)]=age
        else:
            if(age>coordinates[(y,x)]):
                coordinates[(y,x)]=age

    addpeoplePerSec=[list() for _ in range(t)]
    for i in range(t):
        for _ in range(k):
            y,x,age = map(int, sys.stdin.readline().split())
            addpeoplePerSec[i].append( (y,x,age) )

    # print(coordinates)
    # print(addpeoplePerSec)

    for addpeople in addpeoplePerSec:
        for human in addpeople:
            y,x,age = human

            if( (y,x) not in coordinates.keys() ):
                coordinates[(y,x)]=age
            else:
                if(age>coordinates[(y,x)]):
                    coordinates[(y,x)]=age

        print(sum(coordinates.values()))


