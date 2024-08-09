def solution(num, n):
    
    if num % n == 0:
        answer = 1
    elif num % n != 0:
        answer = 0
    
    return answer