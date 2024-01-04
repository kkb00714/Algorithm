# 11. 람다 함수
# => 익명의 함수 / 표현식 이라고도 부름!

# 기본 함수 예제
# def plus_one(x):
#     return x + 1

# print(plus_one(2))

plus_two = lambda x: x + 2 
# lambda 함수는 변수에 할당해줘야 함
# x가 매개변수. x 뒤에 바로 함수 식을 작성
print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_two, a))) 
# a 라는 리스트의 값들을 plus_two 함수에 적용시켜서 출력
# map 은 인자가 두개인 함수 => 여기에선 plus_two가 함수명


# 함수를 따로 만들 필요가 없이, map 에 바로 함수를 표현하는 것이 lambda 함수
print(list(map(lambda x: x + 2, a)))




