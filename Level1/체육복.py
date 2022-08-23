def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost) #여유 체육복 있는 애들 집합
    lost_set = set(lost) - set(reserve)  # 잃어버린 애들 집합 (여유분 있는 애도 잃어버림 가능)
     
    for i in reserve_set:
        if i-1 in lost_set :
            lost_set.remove(i-1)
            
        elif  i+1 in lost_set :
           
            lost_set.remove(i+1)
            answer+=1
    return n-len(lost_set)

print(solution(5,[2, 4],[1,3,5]))