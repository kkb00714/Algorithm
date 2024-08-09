def solution(arr, queries):
    
    answer = arr
    
    # 이번 query는 두개씩.
    # [0, 3], [1, 2], [1, 4] 라고 가정
    # 각 query 마다 순서대로 arr[i] 값과 arr[j]의 값을 바꿈
        # => 먼소리임? 
    # 문제가 이상한듯... 걍 queries 의 배열을 보고 
    # queries 의 [i, j] 에 해당하는 값을 arr 의 배열에서 
    # 바꾸라는 말인 것 같음
    
    for query in queries:
        i, j = query 
        # 인덱스 i, j 를 가져옴
        
        arr[i], arr[j] = arr[j], arr[i]
        # arr[i] 와 arr[j] 의 위치를 서로 바꿈
    
    return answer