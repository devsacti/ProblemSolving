#슬라이싱 1d to 2d
def func1():
    array = [5,11,12,13,14,15,16,17,18,19,20]
    array2d = [array[i:i+array[0]] for i in range(1,len(array),array[0])]
    print([i for i in range(1,10,5)])
    print(array2d)

# transposing matrix
def func2():
    matrix=[[i for i in range(5)] for _ in range(7)]
    print(*matrix,sep='\n')
    matrix=list(zip(*matrix))
    print(*matrix,sep='\n')

    #plus making row 'list'
    print('--making row of matrix as \'list\'--')
    matrix=[list(row) for row in matrix]
    matrix=list(map(list,matrix))

    print(*matrix,sep='\n')

# 매트릭스 반시계 90도 회전
def func3():
    matrix=[[i for i in range(5)] for _ in range(7)]
    print(*matrix,sep='\n')
    matrix=list(zip(*matrix))
    matrix=[list(row) for row in reversed(matrix)]
    print(*matrix,sep='\n')

if __name__=="__main__":
    func2()