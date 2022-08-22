
"""def solution(info, query):
    info_list = [ list(i.split()) for i in info]
    query_list = [ list(i.split()) for i in query]
    answer = [0]*len(query_list)
    
    for i in range(len(query_list)):
        while 'and' in query_list[i]:
            query_list[i].remove('and')
    # 조건만 추출하여 리스트 형태로 저장하는 전처리 
    n=0
    
    #마지막 원소 숫자비교해야해 
    
    for query in query_list: 
        
        for i in range(4):
            cnt=0
            for j in range(4):      
                if query[j] == '-' or query[j] == info_list[i][j]:
                    cnt+=1
                    continue
                else:
                        break

            if cnt == 4 and query[4] <= info_list[i][4]:
                answer[n]+=1
        
        n+=1

    return answer

"""

from itertools import combinations
def solution(info, query):
    answer = []
    db = {}
    for i in info:                   # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]       # 조건들만 모으고, 점수 따로
        score = int(temp[-1])  
        for n in range(5):           # 조건들에 대해 조합을 이용해서  
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:          # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:     # 모든 조건의 경우의 수에 대해 딕셔너리 추가
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():             # 딕셔너리 내 모든 값 정렬
        value.sort()
 
    for q in query:                       # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:                 # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:          
                start, end = 0, len(data)     # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))