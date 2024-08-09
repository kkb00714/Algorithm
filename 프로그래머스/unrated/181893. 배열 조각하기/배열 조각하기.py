def solution(arr, query):
    answer = []
    
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i] + 1]
            
        elif i % 2 == 1:
            arr = arr[query[i]:]
            
    answer.append(arr)
    return arr