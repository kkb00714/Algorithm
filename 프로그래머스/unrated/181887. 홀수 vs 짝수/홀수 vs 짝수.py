def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0: # 짝수일 때
            even_sum += num_list[i]
            
        elif i % 2 == 1: # 홀수일 때
            odd_sum += num_list[i]
            
        answer = max(even_sum, odd_sum)

    
    return answer