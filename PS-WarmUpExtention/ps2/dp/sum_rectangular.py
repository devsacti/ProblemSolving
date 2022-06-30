# summary

# step1

# step2

# step3 implementaion
# runtime error => index error

# make 2d dp table that represents accumulated value from sum of node of matrix[0~givenR][0~givenC]
# based on this definition, DPtable[r][c]=matrix[r][c]+DPtable[r-1][c]+DPtable[r][c-1]-2*(DPtable[r-1][c-1)
# and imagine x+y=k at coord! k is 0,1,2,3, blabla => r+c=k 
def makeDPtable(n,m,matrix):
    # init 2d dptable for 'r+c=k'-oriented access
    DPtable=[[0]*m for _ in range(n)]
    # k == 0 
    DPtable[0][0]=matrix[0][0]
    # k == 1 and check (n,m)=(1,1)
    # ideal : DPtable[r][c]=matrix[r][c]+DPtable[r-1][c]+DPtable[r][c-1]-(DPtable[r-1][c-1])
    # but sometimes part of DPtable[r-1][c]+DPtable[r][c-1]-2*(DPtable[r-1][c-1]) does not exist
    if(n!=1):
        DPtable[1][0]=matrix[1][0]+DPtable[0][0]
    if(m!=1):
        DPtable[0][1]=matrix[0][1]+DPtable[0][0]
    
    for k in range(2,(n-1)+(m-1)+1):
        for nowR in range(k+1):
            # r+c = k => c = k - r
            nowC = k-nowR
            # print(nowR,nowC)
            
            total=0
            if(nowR<0 or nowR>n-1 or nowC<0 or nowC>(m-1)): continue
            
            total+=matrix[nowR][nowC]
            # print('init',total)
            
            if(-1<nowR-1<n):
                total+=DPtable[nowR-1][nowC]
            # print('sub1',total)
            
            if(-1<nowC-1<m):
                total+=DPtable[nowR][nowC-1]
            # print('sub2',total)
            
            if(-1<nowR-1<n and -1<nowC-1<m):
                total-=(DPtable[nowR-1][nowC-1])
                
            DPtable[nowR][nowC]=total
    
    return DPtable

if __name__=="__main__":
    n,m,q = map(int,input().split())
    
    matrix=[]
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    
    quests=[]
    for _ in range(q):
        quests.append(list(map(int,input().split())))
    
    DPtable=makeDPtable(n,m,matrix)
    # print(*DPtable,sep='\n')
    
    for q in quests:
        r1,c1,r2,c2=q
        
        total=DPtable[r2][c2]
        
        borderR=r1-1
        borderC=c1-1
        
        if(-1<borderR<n):
            total-=DPtable[borderR][c2]
            
        if(-1<borderC<m):
            total-=DPtable[r2][borderC]

        if(-1<borderR<n and -1<borderC<m):
            total+=(DPtable[borderR][borderC])
            
        print(total)
