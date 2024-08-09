def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    i = 0
    
    for i in range (len(num_list)):
        if num_list[i] % 2 == 0:
            odd += str(num_list[i])
        elif num_list[i] % 2 == 1:
            even += str(num_list[i])
                    
    sum_odd = int(odd)
    sum_even = int(even)
    
    answer = sum_odd + sum_even
                    
    return answer