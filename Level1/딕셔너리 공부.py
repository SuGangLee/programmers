# x = {} or x= dict() #초기화 
# #추가
# x["key"] = 'value'
# print(x.items()) # -> dict_items([('key', 'value')])
# # 삭제 , 키 값이 기준
# #del x['key']
# #x.pop('key')

# #두 딕셔너리 결합 
# y= {'Ykey':"Yvalue"}

# x.update(y)

# #키 확인
# "키 값" in x # True or False 

# #반복문
# #1. 키 반복 
# for key in x:
#     print(key)
# # 키 목록 리스트 변환 함수
# x.keys()

# for key in x.keys():
#     print(key)

# # 2. 값 반복
# for v in x.values():
#     print (v)

# #3. 키-값 쌍 반복
# for k,v in x.items():
#     print("key [%s] => value [%s]" % (k, v))

####해쉬 사용#####3
# 1. 리스트를 쓸 수 없을 때 
# 리스트는 숫자 인덱스를 이용하여 원소에 접근하는데 즉 list[1]은 가능하지만 list['a']는 불가능합니다.
# 인덱스 값을 숫자가 아닌 다른 값 '문자열, 튜플'을 사용하려고 할 때 딕셔너리를 사용하면 좋습니다.
 
# 2. 빠른 접근  / 탐색이 필요할 때 
#딕셔너리 함수의 시간복잡도는 대부분 O(1)

# 3. 집계가 필요할 때
# 원소의 개수를 세는 문제, 이때 해시와, collections 모듈의 Counter 클래스를 사용하면 아주 빠르게 문제를 푸실 수 있을 것입니다.

#get 메소드: get(key,x)  '딕셔너리에 key가 없는 경우, x를 리턴' 

# 1) Counter 이해하기

# Python이 제공하는 collections 라는 모듈의 한 class이다.
# list를 가지고 Counter를 생성하면, Counter는 Key가 이름이고, Value가 count 인 dictionary를 반환하게 된다. 

#dic = {'a':[1,2,3]}
# dic['a'][0] = 1 , dic['a'].append(4) = >{ 'a':[1,2,3,4]}