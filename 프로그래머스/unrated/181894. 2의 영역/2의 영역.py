def solution(arr):
    answer = []
    index = None
    executed = False
    
    for i in range(len(arr)):
        if arr[i] == 2:
            if index is None and arr[i] == 2:
            # 변수가 아직 설정되지 않았다면 (즉, 처음 2를 발견한 경우) 실행.
            
                index = i
                # 그런 경우, index에 현재 인덱스 i 값을 저장
                
                answer.append(arr[index])
                # 그럼 answer에는 arr[i]인 2 값이 들어가게 됨
                executed = True
                
            else:
                answer = arr[index : i + 1]

    if not executed:
        answer.append(-1)
            
            
    return answer
