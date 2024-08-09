def solution(my_string, queries):
    
    answer = my_string
    
    for query in queries:
        s, e = query
        
        reverse = answer[s : e+1]
        answer = answer[:s] + reverse[::-1] + answer[e + 1:]
            
    return answer