def solution(arr, intervals):
    answer = []
    
    for j, k in intervals:
        for i in range(j, k + 1):
            if i < len(arr):
                answer.append(arr[i])
    
    return answer