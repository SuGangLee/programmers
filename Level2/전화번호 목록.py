#해쉬 
"""
효율성 테스트 실패 
def solution(phone_book):
    answer = True
   #dic = {}

   # for p in phone_book:
    #    dic[p] = 1

   
    for p in phone_book:
        tmp = ""
        for num in p:
            tmp += num  
            #print(tmp)         
            if tmp in phone_book and tmp!=p:
                answer = False
                break

    return answer"""


def solution(phone_book):
    answer = True
    dic = {}

    for p in phone_book:
        dic[p] = 1

   
    for p in phone_book:
        tmp = ""
        for num in p:
            tmp += num  
                    
            if tmp in dic and tmp!=p:
                answer = False
                break

    return answer


print(solution(["119", "97674223", "1195524421"])) 