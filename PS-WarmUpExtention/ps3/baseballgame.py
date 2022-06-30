'''
reference : https://www.acmicpc.net/problem/2503

accurate comprehension
ps1.1.analysis
356 1 0 => 1 strike, 1 ball
...
possible => 324, 328 => 2 cases

ps1.2.drawing pattern,exception
filtering pattern based on tried score by challenger

utilizations and integrations of algorithms
ps2.1.utilization
itertools.permutations for making cases
module 1 : double for ; 1st case of allcases => 2nd filter of filter_val

ps2.2.integration
module 1

Impl
'''

from itertools import permutations

if __name__=='__main__':
    n=int(input())

    # scores for filtering
    filter_scores=[]
    for i in range(n):
        filter_scores.append(list(map(int,input().split())))

    cnt_filters=len(filter_scores)

    # for filter_score in filter_scores:
    #     print(filter_score)

    # 987,986,985,...
    samplespace=[i for i in range(1,10)]
    allcases=list(permutations(samplespace,3))
    # print(allcases)

    validcases=[]

    # greedy check about one candidate case of allcases by filters
    for case in allcases:
        correct=0
        #
        for filter_score in filter_scores:
            std_strike=filter_score[1]
            std_ball=filter_score[2]

            # make filter_num int to list,
            # ex 123->['1','2','3'] for using index of list
            filter_num=list(map(int,str(filter_score[0])))

            # checking per case
            cnt_strike=0
            cnt_ball=0
            
            # ex) 0번째 9, 1번째 8, 2번째 7
            for idx,val_digit in enumerate(case):
                if( (val_digit in filter_num)):
                    if(val_digit==filter_num[idx]):
                        cnt_strike+=1
                    else:
                        cnt_ball+=1
            
            if(std_strike == cnt_strike and std_ball== cnt_ball):
                correct+=1
            else:
                continue

            if(correct==cnt_filters):
                validcases.append(case)

    print(len(validcases))