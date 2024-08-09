def solution(my_string, indices):
    answer = ''
    
    sorted_indices = sorted(indices)
    # indices 의 문자열을 오름차순으로 정렬함
    current_index = 0
    
    # 인덱스를 건너뛰면서 문자열을 이어붙임
    for index in sorted_indices:
        answer += my_string[current_index:index]
        # 현재 인덱스부터 index까지의 문자열을 붙임
        current_index = index + 1
        # 현재 인덱스를 index + 1로 업데이트하여 해당 문자를 건너뜀
    
    answer += my_string[current_index:]
    
    return answer