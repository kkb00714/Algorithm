def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        reverse_str = int(intStrs[i][s:s+l])
        
        if reverse_str > k:
            answer.append(reverse_str)
            
    
    return answer