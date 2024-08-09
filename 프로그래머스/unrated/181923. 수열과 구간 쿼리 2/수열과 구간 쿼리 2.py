def solution(arr, queries):
    
    answer = []
    
    # (크기) s < i < e 
    # (순서) s, e, k => k 보다 크면서 가장 작은 arr[i] 찾기
    
    # ex) queries 의 값이 [0, 4, 2], [0, 3, 2] 일 경우
    # 각 quaries의 s, e, k 값은 각각 0, 4, 2 / 0, 3, 2 임
    # 따라서 i 값도 각각 0 <= i <= 4 / 0 <= i <= 3 
    # => k 값은 query에 따라 다르고(???) 으아아 암튼 
    # 첫번째 k값은 2 , 두번째 k 값은 2 
    # 아 이해됏다
    
    # 1) 주어진 배열(arr) 에 대해 각 query가 주어짐
    # 2) 각 query는 (s, e, k) 로 이루어져 있음
    # 3) 각 query마다 주어진 범위 's' 부터 'e' 까지 해당 범위에 있는 값 i에 대한 arr[i] 값 중에서 'k' 보다 크면서 가장 작은 값을 찾아야 함
    # 4) 해당 값을 찾으면 그 값을 배열에 저장, 못 찾으면 -1 저장
    
    for query in queries:
        query_list = []
        # queries 값들을 모두 비교해야 하므로 빈 리스트 생성
        
        for i in range(query[0], query[1] + 1):
        # query[0] 에서 query[1] 까지의 범위를 잡음
        
            if arr[i] > query[2]:
                query_list.append(arr[i])
        # 만약 arr[i] 에 있는 원소가 query[2] 보다 크다면
        # arr[i] 를 query_list 에 추가
        
        try:
            answer.append(min(query_list))
        # query_list 에서 가장 작은 값을 찾아 answer에 추가
        except:
            answer.append(-1)
        # 못 찾았으면 answer에 -1 추가
            
    return answer