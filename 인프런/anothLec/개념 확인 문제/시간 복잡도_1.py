# 시간 복잡도 
# => 입력값의 변화에 따라 연산을 시행할 때, 
# 연산 횟수에 비해 시간이 얼마나 걸리는지 고려하는 것

# 효율적인 알고리즘
# => 입력값이 커짐에 따라 증가하는 시간의 비율을 최소화한 알고리즘

# 시간 복잡도 최악의 경우도 고려하여 대비

# Big-O 표기법의 종류
# O(1)
# O(n)
# O(log n)
# O(n2)
# O(2n)

# O(1) 의 시간 복잡도를 가진 알고리즘
# => 입력값의 크기와 관계없이, 즉시 출력값을 얻어낼 수 있음을 의미

def O_1_algorithm(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5]
index = 1
result = O_1_algorithm(arr, index)
print(result) # 2

# O(n) "
# => 선형 복잡도(linear complexity) 라고도 불리며
# => 입력값이 증가함에 따라 시간또한 같은 비율로 증가
# ex) 입력값이 1일 때 걸리는 시간이 1초일 때, 입력값이 100일 때는 걸리는 시간이 100초

# 입력값이 증가함에 따라 같은 비율로 걸리는 시간이 늘어남
# 입력값이 커질수록 계수(n 앞에 있는 수)의 의미가 점점 퇴색
# => 같은 비율로 증가하고 있다면, 계수 상관없이 O(n) 으로 표현

def O_n_algorithm(n) :
    for i in range(n):
        i += 1
        
def O_n_algorithm2(n) :
    for i in range(2 * n):
        i += 1
    

# O(log n)
# => 로그 복잡도(logarithmic complexity) 라고 부르며
# => Big-O 표기법 중 O(1) 다음으로 빠른 시간 복잡도를 가짐


# O(n2)
# => 2차 복잡도(quadratic complexity) 
# => 입력값이 증가함에 따라 시간이 n의 제곱수의 비율로 증가
# => n이 커지면 커질수록 지수가 주는 영향력이 점점 퇴색


# O(2n) 
# => 기하급수적 복잡도(exponential complexity) 
# => Big-O 표기법 중 가장 느린 시간 복잡도

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# => 재귀로 구현하는 피보나치 수열은 O(2n)의 시간복잡도를 가진 대표적 알고리즘
