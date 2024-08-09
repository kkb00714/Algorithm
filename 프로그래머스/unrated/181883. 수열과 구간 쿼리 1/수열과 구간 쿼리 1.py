def solution(arr, queries):
    
    for query in queries:
        s, e  = query
        
        for i in range(s, e+1):
            if  s <= i and i <= e:
                arr[i] += 1
    
    return arr