# 정렬 관점에서 해시를 바라보고, 그 반대를 해보고
# 3,32,324,...가 되는데 56

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    len_phone_book=len(phone_book)
    
    # print(phone_book)
    
    if(len_phone_book==1):
        answer = True
    else:
        for idx in range(len_phone_book-1):
            len_before=len(phone_book[idx])
            if(phone_book[idx] in phone_book[idx+1][:len_before]):
                answer=False
                break
            
    
    return answer