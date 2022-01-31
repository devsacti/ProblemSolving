'''
reference : https://www.acmicpc.net/problem/2578

ps1. accurate comprehension
ps1.1. analysis
1. 선이 3개 이상일 때 빙고

ps1.2. drawing pattern, exception
5번 체크 이상 부터 가로, 세로, 대각선 빙고여부를 체크


ps2. utilizations and integrations of computer algorithms
ps2.1. Util
모듈1 체크는 빙고판에서 목표 숫자의 row,col 확인 후 별도의 빙고체크 매트릭스에 체크
모듈2 빙고체크 매트릭스에 대한 가로, 세로, 대각선 체크

ps2.2. Integ
모듈1 => 모듈2

ps3. Impl
'''
# check bingoMatrix by checkMatrix
def checkbingo(cur_num,bingoMatrix,bingocheckMatrix):

    for r in range(n):
        # 추후 break 추가
        for c in range(n):
            if(bingoMatrix[r][c]==cur_num):
                bingocheckMatrix[r][c]='*'
                break
    
    # 형식상 리턴
    return bingocheckMatrix

# check bingo horizontal, vertical, diagonal
def checkBingoCount(bingocheckMatrix):

    cnt_bingo=0

    # check horizontal bingo
    for r in range(5):
        cnt_check=0
        for c in range(5):
            if(bingocheckMatrix[r][c]=='*'):
                cnt_check+=1
                if(cnt_check>=5):
                    cnt_bingo+=1

    # check vertical bingo
    for c in range(5):
        cnt_check=0
        for r in range(5):
            if(bingocheckMatrix[r][c]=='*'):
                cnt_check+=1
                if(cnt_check>=5):
                    cnt_bingo+=1
    
    # previous method is get the val of dignomal and using for, this time is the other
    ## digonal sub 1.
    cnt_check=0
    for r in range(5):
        c=r
        if(bingocheckMatrix[r][c]=='*'):
            cnt_check+=1
            if(cnt_check>=5):
                cnt_bingo+=1

    ## digonal sub2.
    cnt_check=0
    for r in range(5):
        c=4-r
        if(bingocheckMatrix[r][c]=='*'):
            cnt_check+=1
            if(cnt_check>=5):
                cnt_bingo+=1


    return cnt_bingo

if __name__=='__main__':
    n=5

    bingoMatrix=[]

    for i in range(n):
        bingoMatrix.append(list(map(int, input().split())))

    givenNums=[]

    for i in range(n):
        givenNums.extend(list(map(int, input().split())))
    
    #print(*bingoMatrix,sep='\n')
    #print(givenNums)

    bingocheckMatrix=[[0]*n for _ in range(n)]

    # 추후 5번째 숫자부터 체크하는 예외처리 기입
    cnt_bingo=0
    for ordinal_idx, num in enumerate(givenNums,1):
        # check num in bingoMatrix
        bingocheckMatrix=checkbingo(num,bingoMatrix,bingocheckMatrix)
        # print(*bingocheckMatrix, sep='\n')

        # check bingo
        cnt_bingo=checkBingoCount(bingocheckMatrix)
        # print('==', ordinal_idx, cnt_bingo)

        # check bingo cnt and break and return order
        if(cnt_bingo>=3):
            print(ordinal_idx)
            break
