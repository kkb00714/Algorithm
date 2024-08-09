def solution(num_list):
    answer = 0
    
    for i in range(len(num_list)):
        while num_list[i] != 1:
            if num_list[i] % 2 == 0:
                num_list[i] = num_list[i] / 2
                answer += 1
            elif num_list[i] % 2 == 1:
                num_list[i] = (num_list[i] - 1 ) / 2
                answer += 1
    
    return answer