
#점수가 제일 높은 순, 동점일 경우, 사전 순 

def solution(survey, choices):
    score = [0,3,2,1,0,1,2,3]
    type = {'T':0,'R':0,'C':0,'F':0,'M':0,'J':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] >= 4:
            type[survey[i][1]]+=score[choices[i]]
        else: 
             type[survey[i][0]]+=score[choices[i]]
    answer=''

    if type['T'] <= type['R']:
        answer+='R'
    else: 
        answer+='T'
    
    if type['F'] <= type['C']:
        answer+='C'
    else: 
        answer+='F'

    if type['M'] <= type['J']:
        answer+='J'
    else: 
        answer+='M'

    if type['N'] <= type['A']:
        answer+='A'
    else: 
        answer+='N'
   
        
    return answer 

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = 	[5, 3, 2, 7, 5]	
result = "TCMA"
print(solution(survey,choices))