def solution(num_list):
    sum_of_element = 0
    square_of_element = 1
    i = 0
    
    for i in range(len(num_list)):
        # 리스트의 길이만큼 반복
        sum_of_element += num_list[i]
        # 모든 원소들의 합
        square_of_element *= num_list[i]
        # 모든 원소들의 곱
        
    square = sum_of_element ** 2
    # 모든 원소들의 합의 제곱
    
    if square_of_element < square:
        return 1
    else:
        return 0
