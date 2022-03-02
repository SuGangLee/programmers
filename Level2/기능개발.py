def my_solution(progresses, speeds):
    answer = []
    time = [0]*len(speeds)
    count=1
    for i in range(len(progresses)):
        while(progresses[i] < 100 ):            
            progresses[i]+=speeds[i]
            time[i]+=1
    
    for i in range(1,len(time)):
       # print("i: ",i)
        if time[i-1] >= time[i]:
            
            count+=1
            time[i]=time[i-1]
           # print("time:",time)  
                       
        else: 
            answer.append(count)
            count=1
            #print(i,",",answer)
    answer.append(count)
   
    
    return answer

print(my_solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	))


#zip은 리스트를 튜플로 묶어줌 ex) [1,2],[a,b] -> [(1,a),(2,b)] / unzip 가능 

def other_solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds): 
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]