def solution(arr, queries):
    answer = arr[:]
    # arr 배열을 복사해서 answer에 대입
    
    # queries 안의 query => 2차원 배열 형태로 존재
    # 2차원 배열에서 [s, e, k] 순서로 존재함
    # 각 query마다 s <= i <= e 인 모든 i 에 대해, 
    # i가 k 의 배수이면 arr[i] + 1 
    
    for query in queries:
        s, e, k = query
        # 각 query에서 s, e, k 를 가져옴
        
        for i in range(s, e + 1):
            if i % k == 0:
                answer[i] += 1
            # answer 리스트는 arr의 복사본이므로, 
            # answer.append() 를 통해서 원소를 추가하면 
            # arr에는 요소가 추가되지 않으므로
            # answer[i] += 1 을 통해 answer에 직접적으로 추가해줌
    
    return answer