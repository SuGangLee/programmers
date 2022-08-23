def solution(arr): 
    stack = [arr[0] ] # or stack = []
    for i in arr:
        if stack[-1] == i:   # stack [-1:] == [i] 
            continue 
        stack.append(i)
    return stack

arr = [1,1,3,3,0,1,1]

print(solution(arr))