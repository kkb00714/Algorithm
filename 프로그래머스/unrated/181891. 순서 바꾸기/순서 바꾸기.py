def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    
    # num_list[n - 1] , num_list[n] 으로 나눠서
    # n번째(num_list[n]) 이후 원소들을 
    # n 번째까지의(num_list[n-1]) 원소들 앞에 붙이기


    return answer