def solution(numbers, n):
    answer = 0

    for i in range(len(numbers)):

        if answer <= n:
            answer += numbers[i]
            
    return answer