def solution(a, b):
    
    str1 = int(str(a) + str(b))
    str2 = int(2 * a * b)
    answer = 0

    if str1 < str2:
        answer = max(str1, str2)
    
    else:
        answer = str1
        
    return answer