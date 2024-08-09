# a, b = input().strip().split(' ')
# b = int(b)

a, b = input().strip().split(' ')
# 입력받은 문자열을 공백을 기준으로 분할하고,
# 그 변수를 각각 a, b 에 할당함

b = int(b)
# 입력받은 b의 값을 int(정수형) 으로 변환

if 1 <= b <= 5:
    print(a * b)
        
    

