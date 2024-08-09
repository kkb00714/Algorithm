def solution(my_string, overwrite_string, s):
    
    str1 = my_string[:s] 
    # 문자열 my_string 에서 처음부터 s번째 인덱스 이전까지의 문자열을 str1에 할당
    str2 = my_string[s + len(overwrite_string):]
    # my_string 문자열에서 overwrite_string의 문자열의 길이에 + s를 더해서 시작 인덱스를 계산함
    
    answer = str1 + overwrite_string + str2
    
    return answer