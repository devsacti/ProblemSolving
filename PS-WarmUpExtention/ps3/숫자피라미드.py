'''
reference : 알고리즘잡스 L2,
sub reference(unstable) : https://haejun0317.tistory.com/13

accurate comprehension
ps1.1
pyramid pattern
numbering ; 1 ~, and odd index of row ; right to left, even index of row ; left to right
'10 becomes 1' 

ps1.2

utilizations and integrations of algorithms
ps2.1
Module 1.1 : pyramid pattern => 1,3,5,7,... pieces from sample ; total cnt is n*n
Module 1.2 : '10 becomes 1' => samplespace 1~9
Module 2 : index of row => if idx%2==1

ps2.2
Module 1.2 => Module 1.1 => Moudle 2

Impl

'''
if __name__=="__main__":
    n,s = map(int, input().split())
  
    # Module 1.2    
    # samplespace
    samplespace=[i for i in range(1,10)]
    
    # sampling from samplespace
    start_idx=samplespace.index(s)
    cnt_sampling=n*n
  
    sample=[]
    while(cnt_sampling>0):
        sample.append(samplespace[(start_idx%9)])
        
        start_idx+=1
        cnt_sampling-=1
    
    # print(sample)
    
    # Module 1.1
    # count of item of row of pyramid
    # pattern 2*n+1
    cnt_item_row=[2*n+1 for n in range(n)]
    
    s_idx=0
    e_idx=0
    
    pyramid={}
    
    for num, cnt in enumerate(cnt_item_row,1):
        e_idx=s_idx+cnt
        
        # Module 2
        
        if(num%2==1):
            pyramid[num]=list(reversed(sample[s_idx:e_idx]))
        else:
            pyramid[num]=sample[s_idx:e_idx]
        s_idx=e_idx
        
    for k,v in pyramid.items():
      print(' '*(n-k),end="")
      print("".join(map(str,v)))
      
