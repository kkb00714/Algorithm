# 8. 리스트와 내장함수(2)

a = [23, 12, 35, 63, 19]
print(a[:3]) # 리스트의 2번째 인덱스까지 출력
print(a[0:2]) # 인덱스 0부터 1까지 출력
print(a[0:5:2]) # 인덱스 0부터 4까지 2씩 증가
print(len(a))

for i in range(len(a)):
    # a의 길이만큼 i가 증가
    print(a[i], end=' ')
print()

for x in a:
    # a의 리스트에 있는 값을 a가 차례차례 접근함
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x)
print()

for x in enumerate(a):
    # 인덱스 번호와 함께 같이 접근할 때 사용
    # 튜플 형태로 반환됨 
    # ex) (0, 23), (1, 12), (2, 35) ...
    print(x)
print()

b = (50, 40, 30, 20, 10) 
# print(b[0])
# b[0] = 7
# 튜플을 값 변경이 안됨

for x in enumerate(a):
    print(x[0], x[1])
    # x의 원소값을 출력할 때 이런식으로 출력
print()

for index, value in enumerate(b):
    print(index, value)
print()

if all(60 > x for x in a):
    # a 라는 리스트에 x가 접근,
    # 그 x값을 조건문(60 > x)에 계속해서 비교. 
    
    # all 함수 => 조건이 하나라도 거짓이 되면, 
    # 거짓을 return 하고, 모두가 다 참이면, 참을 반
    print("YES")
else:
    print("NO")


if all(10 < x for x in a):
    print("YES")
else:
    print("NO")




