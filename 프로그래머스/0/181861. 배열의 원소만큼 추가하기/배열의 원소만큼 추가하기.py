def solution(arr):
    answer = []
    for x in arr:
        for y in range(x):
            answer.append(x)
    
    return answer