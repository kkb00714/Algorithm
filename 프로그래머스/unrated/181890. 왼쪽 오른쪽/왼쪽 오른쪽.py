def solution(str_list):
    answer = []
    
    # if l이 먼저 => 해당 문자열 기준 왼쪽에 있는 문자열을 순서대로 담음
    # if r이 먼저 => 해당 문자열을 기준으로 오른쪽에 있는 문자열을 순서대로 담음. 
    # 선택된 문자열들은 삭제되는듯
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            answer = str_list[:i]
            break
        elif str_list[i] == 'r':
            answer = str_list[i + 1:]
            break

    return answer