# 10. 함수 

# def add (a, b):
#     c = a + b
#     print(c)
    
# add(1, 5)

# def add(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#     # 값을 리턴하고 함수가 종료됨

# print(add(3, 2))
# 반환한 결괏값을 함수가 받음.


def isPrime(x):
    for i in range(2, x): 
        # 2부터 자기 자신 전(x-1)까지 범위 지정
        if x % i == 0: 
            # 나누어 떨어지는 게 하나라도 있으면
            return False
    return True 
    # 전부 나누어 떨어지지 않을 경우 (자기 자신 외 약수가 없을 경우)
        
a = [12, 13, 7, 9, 18]
for y in a:
    if isPrime(y):
        print(y, end=' ')





