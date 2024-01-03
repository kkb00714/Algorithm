# 2. 변수 입력과 연산자
# Tip!! 형 결정)  정수 + 실수 = 실수 

a, b = input("두 숫자를 입력하세요: ").split()
print(type(a), type(b), sep='\n')

a, b = map(int, input("두 숫자를 입력하세요: ").split())
# map은 두개의 인자.
# 두 개의 숫자를 split하여 받고 int로 인해 정수화 시킨 후 각 값을 매핑
print(type(a), type(b), sep='\n')

print(a+b, a-b, a*b, a/b, a//b, a%b, a**b,sep='\n')

# 헷갈림 주의!
# / 는 나누기
# // 는 a를 b로 나눈 몫을 구해줌
# % 는 a를 b로 나눈 나머지를 구해줌
# ** 는 a를 b제곱한 값을 구해줌 (a^b)

a, b = map(str, input("두 문자를 입력하세요: ").split())
print(type(a), type(b), sep='\n')




