def solution(my_string, s, e):
    
    answer = ''

    if 0 <= s <= e <= len(my_string):
        answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
        # 인덱스 s 부터 e까지 (포함) 의 문자열을 가져옴
        # [::-1] 부분은 문자열을 거꾸로 뒤집어서 나열함
        # 따라서 my_string[s:e+1] 의 범위까지 거꾸로 뒤집을 값을 answer에 대입함
    
    return answer