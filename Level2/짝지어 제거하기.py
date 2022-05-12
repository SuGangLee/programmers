#stack 사용
def solution(s):
    stack =[]
    answer=0

    for i in s:
        if len(stack) ==0 : stack.append(i)
        elif stack[-1] == i : stack.pop()
        else : stack.append(i)
    
    if len(stack)==0: answer=1
             
    return answer

print(solution("ccdd"))