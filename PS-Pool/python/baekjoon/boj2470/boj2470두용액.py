'''
ps1. accurate comprehension
ps1.1. analysis

ps1.2. drawing pattern, exception
pattern1 본문의 특성값 개념을 그대로 bs를 구현하려고 했지만, 처음 도출된 값과 비교해서
왼쪽으로 갈지, 오른쪽으로 갈지 결정할 값이 마땅치 않음
=> 주어진 값중에 그런 것이 없다면, 좌우를 살펴서 이동할수있다!,
이를 pattern2에 혼용

pattern2 우선 Ideal 상황을 가정하고 근사화!+ Empircal!
std와 동일하거나 유사한 값을 찾을려고 노력해보면,
기준과 타겟의 합의 절대값, 즉 특성값이 0이면 스탑

당장 수학적 설명은 모르겠다! nums 정렬 후 기준값마다 특성값 나열하면 오른쪽으로 증가한다.
일단 최초 정렬을 통해 오른쪽으로 갈수록 양수이나 절대값측면에서는 알수없다.
이부분이 혼동이나 어쨌거나 특성값은 abs(std)+ abs(experi)가 아니다.
abs(std+experi) 이므로, experi가 증가할수록 특성값의 이전, 원시값이 커지므로 절대값도 커진다!

=> 전체적인 패턴이 아니었음. 음수+양수인 경우에 한해서 성립하는 패턴이었음
반례)
std = -99 , nums=[-99, -2, -1, 4, 98]
다만, 결과값이 양의 이차함수 꼴임 U패턴, 

종합해보니, 위 성질로 인해서 따로 left, right로 로컬 극소값 구하면 ㄷ됨       

ps2. utilizing and integration of computer algorithms
ps2.1.

!! exception
언제나 점이 3개 아니라서, 별도의 예외처리가 필요하다. 2개에 따른 비교 혹은 3개에 따른 비교를
세분화하거나, 리스트가 증가하는지 감소하는지 체크필요.
=> 새로운 내장함수 이용

# check if it is sorted in ascending order
is_sorted = all(x<y for x, y in zip(ages[:-1], ages[1:]))

# check if it is sorted in descending order
is_sorted = all(x>y for x, y in zip(ages[:-1], ages[1:]))


ps2.2.

        # finding minimum extreme value
        if( all(x<=y for x, y in zip(experi_val_li[:-1], experi_val_li[1:])) ):
            bestpair_index=mid
            e=mid-1
        elif( all(x>=y for x, y in zip(experi_val_li[:-1], experi_val_li[1:])) ):
            bestpair_index=mid
            s=mid+1
        else:
            # local minimum extreme value(s)에 도달한 경우 ; that canbe 'f'(x) is 0' at the ideal quadratic fomular
            bestpair_index=mid
            break

!! 시간 초과 생각해보면 어쨌거나 *3이 되서 애당초, 최소 2~3칸이 되게 샘플링하는게 더 빠른가봄

=> 하지만 애당초 위와같이 1번의 주기마다 주변 3개를 실행하다보면 타임아웃뜨는듯,
=> 최악의 경우에 대해서 위와같은 #finding minimum extreme value는 언제나 시간초과가 뜨는 것으로 보인다.
=> 다른 방식을 찾아야한다.

ps3. Impl
'''
def bs(std,idx_std,nums,s,e):
    
    std_s=s
    std_e=e
    # print(nums,s,e)

    bestpair_index=-1
    
    while(s<=e):
        mid=(s+e)//2
        # print('s',s,'mid',mid,'e',e)
        
        # custom part ; VALID left of mid, mid, right of mid
        experi_idx_li=[mid]
        if(std_s<=mid-1<=std_e): experi_idx_li = [mid-1] + experi_idx_li
        if(std_s<=mid+1<=std_e): experi_idx_li = experi_idx_li + [mid+1]

        experi_val_li=[]
        for cand_idx in experi_idx_li:
            experi_val_li.append( abs(std+nums[cand_idx]) )
        
        # finding minimum extreme value
        if( all(x<y for x, y in zip(experi_val_li[:-1], experi_val_li[1:])) ):
            bestpair_index=mid
            e=mid-1
        elif( all(x>y for x, y in zip(experi_val_li[:-1], experi_val_li[1:])) ):
            bestpair_index=mid
            s=mid+1
        else:
            # local minimum extreme value(s)에 도달한 경우 ; that canbe 'f'(x) is 0' at the ideal quadratic fomular
            bestpair_index=mid
            break

    bestpair_val=nums[bestpair_index]
    best_feature_val= abs(std+bestpair_val)

    # 근방까지 최대 3개라 아래와같이 접근
    if(bestpair_index==idx_std):
        min_idx=-1
        min_val=int(1e20)
        for experi_idx,experi_val in zip(experi_idx_li,experi_val_li):
            # print(pair)
            if(experi_idx==idx_std):
                continue
            else:
                if(experi_val<min_val):
                    min_val=experi_val

                    min_idx=experi_idx
                    min_pair_val=nums[min_idx]
                    min_feature_val=abs(std+min_pair_val)
        
        bestpair_index=min_idx
        bestpair_val=min_pair_val
        best_feature_val=min_feature_val

    # best idx, value,특성값 
    return bestpair_index, bestpair_val,best_feature_val

if __name__=="__main__":
    
    n=int(input())
    
    nums=list(map(int,input().split()))
    nums.sort()
    
    answer=""
    global_min_feature_val=int(1e12)
    
    # start index, end index
    s=0
    e=len(nums)-1
    
    for idx_std,std in enumerate(nums):
        # print('##',std)
        # 자기자신과 짝지어지는 것을 사전에 방지하기 위해, check대상이 되는 리스트는 현재 std를 뺀다.
        # => 시도 결과 시간초과 케이스가 더 늘어남, 도로묵

        # tmp_nums=nums[:]
        # del tmp_nums[idx_std]
        
        idx_pair,val_pair, feature_val=bs(std, idx_std, nums, s, e)
        # print('###',idx_pair,val_pair,feature_val)

        if(feature_val==0):
            global_min_feature_val=feature_val
            answer=str(std)+" "+str(val_pair)
            break

        if(feature_val<global_min_feature_val):
            global_min_feature_val=feature_val
            answer=str(std)+" "+str(val_pair)
    
    print(answer)