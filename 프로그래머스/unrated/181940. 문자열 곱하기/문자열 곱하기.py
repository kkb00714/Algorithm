def solution(my_string, k):
    
    if 1 <= k <= 100:
        if 1 <= len(my_string) <= 100:
            answer = my_string * k
    return answer