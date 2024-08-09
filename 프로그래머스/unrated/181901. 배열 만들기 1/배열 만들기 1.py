def solution(n, k):
    answer = []
    
    # n이 k의 배수일 때 => if n % k == 0
    
    for i in range(1, n + 1):
        # 1부터 n 까지 반복
        
        if i % k == 0:
            answer.append(i)
    
    return answer