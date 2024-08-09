def solution(n):
    
    answer = 0
    
    if n % 2 != 0: # 홀수일 때
        for i in range (1, n + 1, 2):
            answer += i
    
    if n % 2 == 0: # 짝수일 때
        for i in range (2, n + 1, 2):
            answer += i ** 2
            # 파이썬에서는 제곱을 ** 로 표현
            
# range(1, n + 1, 2)
# 시작 값 (start): 1
# 끝 값 (stop): n + 1 (n + 1은 범위에 포함되지 않음)
# 스텝 값 (step): 2 (홀수만 선택)
# => 따라서 1 부터 n+1 값까지 2씩 뛰어서 선택 !
    
    
    return answer