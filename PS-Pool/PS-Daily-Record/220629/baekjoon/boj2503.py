# ps1. comprehension
## analysis

## drawing pattern

## approach ; bruteforce

# ps2. applying algortihms

# ps3. Impl
from itertools import permutations

if __name__=="__main__":
    n=int(input())
    records=[]

    for _ in range(n):
        item, strike_cnt, ball_cnt=list(map(int,input().split()))
        try_val=list(map(int,str(item)))

        record=[try_val,strike_cnt,ball_cnt]
        records.append(record)

    # print(records)

    samplespace=[i for i in range(1,10)]
    allcases=list(permutations(samplespace,3))

    # print(len(allcases))

    fits=[]

    for case in allcases:
        # print('#input case',case)
        valid_token=True

        for record in records:
            ask_val, strike_cnt, ball_cnt = record

            experi_strike=0
            experi_ball=0
            
            for idx, experi_val in enumerate(case):
                if(experi_val in ask_val):
                    if(idx==ask_val.index(experi_val)):
                        experi_strike+=1
                    else:
                        experi_ball+=1
            # print('## ck',experi_strike,experi_ball)

            if(experi_strike==strike_cnt and experi_ball==ball_cnt):
                # print('sub valid')
                pass
            else:
                valid_token=False
                break

        if(valid_token):
            fits.append(case)
    
    # print(fits)
    print(len(fits))


