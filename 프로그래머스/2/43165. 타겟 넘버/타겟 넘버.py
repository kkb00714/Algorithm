def solution(numbers, target):
    answer = 0
    
    def dfs(L, cnt):
        nonlocal answer
        
        if L == len(numbers):
            if cnt == target:
                answer += 1
        else:
            dfs(L+1, cnt + numbers[L])
            dfs(L+1, cnt - numbers[L])
            
    dfs(0, 0)
    
    return answer