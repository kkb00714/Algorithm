def solution(str1, str2):
    answer = ''
    
    if 1 <= len(str1) and len(str2) <= 10:
        for i in range (len(str1)):
            answer += str1[i] + str2[i]
    
    return ''.join(answer)