def solution(arr, idx):
    answer = -1
    
    for i in range(len(arr)):
        if arr[i] == 1 and (answer == -1 and i >= idx):
            answer = i
            

    return answer