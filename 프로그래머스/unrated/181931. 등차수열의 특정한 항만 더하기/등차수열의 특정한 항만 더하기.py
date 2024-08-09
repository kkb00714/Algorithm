def solution(a, d, included):
    answer = 0
    numerical = a
    
    for i in range(len(included)):
        if included[i]:
            answer += numerical
        numerical += d 
        # 다음 항으로 이동
    
    return answer