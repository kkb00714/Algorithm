def solution(todo_list, finished):
    answer = []

    for a, b in zip(todo_list, finished):
        # todo_list와 finished의 각 요소를
        # 동시에 가져와서 a, b에 할당
        
        if b == False:
            # b가 False 라면 a를 answer에 추가
            # b가 boolean 값 False, True 이므로 대문자로 작성
            answer.append(a)
    
    return answer