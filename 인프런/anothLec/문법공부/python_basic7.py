# 7. 리스트와 내장함수(1)

import random as r
# (random 모듈을 r로 명령하겠다는 의미)
# 무작위로 섞을 때, random이라는 모듈에 있는 shuffle 사용 

# a = []
# print(a)
# b = list()
# print(b)

a = [1, 2, 3, 4, 5, 6]
# print(a)

b = list(range(1, 11))
# print(b)

c = a + b
# print(c)
a.append(7)
print(a)

a.insert(4, 7) # 4번 인덱스에 7을 넣는다는 의미
print(a)

a.pop() # 가장 마지막에 있는 인덱스의 값 제거
print(a) 

a.pop(3) # 특정 인덱스의 값 제거
print(a) 

a.remove(6) # 인덱스의 값 중에 6이라는 값을 제거
print(a)

print(a.index(5)) # a의 5번 인덱스를 출력

a = list(range(1, 11))
print(a)
print(sum(a)) # a라는 리스트에 있는 값들을 전부 합해서 출력
print(max(a)) # a라는 리스트에서 가장 큰 값을 출력
print(min(a)) # a라는 리스트에서 가장 작은 값을 출력

print(max(7, 5), min(1, 3)) 
# max나 min은 인자값들 중에서 최대 최솟값을 찾아줌

r.shuffle(a)
print(a)

a.sort() # 오름차순으로 정렬 (원본을 정렬하고 수정함)
print(a)

a.sort(reverse=True) # 내림차순으로 정렬 (원본을 역정렬하고 수정함)
print(a)

a.reverse() # 원본 순서를 뒤집고 수정
print(a)

a.clear() # 리스트에 있는 값들을 모두 삭제
print(a)



