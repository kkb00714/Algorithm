def solution(num_list):
    answer = num_list
    
    # 1) 마지막 원소 > 이전 원소 => 마지막 원소 - 이전 원소
    # 2) 마지막 원소 < 이전 원소 => 마지막 원소 * 2
    
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])

    elif num_list[-1] <= num_list[-2]:
        answer.append(num_list[-1] * 2)
    
    return answer