def solution(my_string, m, c):
    answer = ''
    

    for i in range(0, len(my_string), m):
        split_string = my_string[i:i + m]
        # m 만큼의 길이만큼 문자열을 끊어서 split_string에 할당
        
        # 이제 리스트[i]의 c 번째 인덱스를 출력하는 코드 필요
        if c - 1 < len(split_string):
            answer += split_string[c - 1]
        
    return answer
