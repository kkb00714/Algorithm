def solution(my_string, is_prefix):
    answer = 0
    prefix = []
    
    
    for i in range(len(my_string)):
        prefix.append(my_string[:i])
    
    if is_prefix in prefix:
        answer = 1
        
    return answer
            
