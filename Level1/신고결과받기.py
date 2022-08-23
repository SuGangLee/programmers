def solution(id_list, report, k):
    dic = { i : [0] for i in id_list}
    result = [0] * len(id_list)
    stoped_id_list = []
    for i in report :
        a,b = i.split(' ')
        if b in dic[a]:
            continue
        dic[a].append(b)
        dic[b][0]+=1
        print(dic)
        if dic[b][0] == k:
            stoped_id_list.append(b)
    for stoped in stoped_id_list:
        for i in range(len(id_list)):
            if stoped in dic[id_list[i]]:
                result[i]+=1

    
    return result

#동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"]
,3))

