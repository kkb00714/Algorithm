def solution(my_string, index_list):
    
    # index_list 의 값에 따른 my_string 의 인덱스 값 이어서 출력
    
    answer = ''.join([my_string[i] for i in index_list])
    # index_list에 있는 각 인덱스 i 에 대해 my_string[i] 를 추출하여 새로운 리스트인 answer에 할당함.
    
    # ''는 빈 문자열을 의미하며, 새로운 리스트인 answer에 원소를 추가할 수 있도록 미리 초기화 해둔 것.
    # .join => join 메서드로, 리스트의 원소들을 하나의 문자열로 연결함. 
    # (이 때, join 메서드의 인자로 전달된 문자열을 사용하여 리스트의 원소들을 이어붙임)
    # 
    
    return answer