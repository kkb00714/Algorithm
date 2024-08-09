def solution(my_string, is_suffix):
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i:].endswith(is_suffix):
        # 특정 인덱스 i 부터 시작하여 해당 위치부터 끝까지 is_suffix와 같은지 확인하는 코드
        # endswith(is_suffix) => 이 부분 문자열이 is_suffix로 끝나는지 검사함
            answer = 1
            break
            
    return answer