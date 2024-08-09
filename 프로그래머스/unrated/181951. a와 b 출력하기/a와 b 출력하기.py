# a, b = map(int, input().strip().split(' '))
# print(a + b)

# map(function, iterable, ...)
# function은 각 요소에 적용할 함수를 지정,
# iterable은 함수를 적용할 순회 가능한(iterable) 객체를 지정

# strip : 입력 문자열의 양 끝에 있는 공백 제거
# split(' ') : 문자열의 공백을  기준으로 분할하여 문자열의 리스트 생성
# map(int, ...) : 분할된 문자열 리스트의 각 요소를 정수로 변환 => 변환된 것을 각각 a, b에 저장함


a, b = map(int, input().strip().split(' '))

print("a =", a)
print("b =", b)





