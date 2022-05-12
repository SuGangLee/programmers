def solution(n, times):
    answer = 0
    cost = []
    waste = times.copy()
    s=0
    for i in range(n):
        mindex = times.index(min(times))
        mins= min(times)
        print(mindex)
        cost.append(mins)
        times.insert(mindex,mins+waste[mindex])
        times.remove(mins)
        
        print(times)
        
    print(cost)
    
    return cost[-1]

print(solution(6,[7,10])) 

