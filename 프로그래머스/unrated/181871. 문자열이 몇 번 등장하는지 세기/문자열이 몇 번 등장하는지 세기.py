def solution(myString, pat):
    answer = 0
    start = 0
    
    while True:
        
        result = myString.find(pat, start)
        # 문자열.find(pat, start) 
        # => myString[start] 부터 pat으로 시작하는 문자열을 찾아줌
        # => 만약 찾지 못하면 -1 반환

        # result에는 현재 myString에서 pat을 찾은 위치를 저장
        
        if result != -1:
            answer += 1
            start = result + 1
            
        else:
            break
        
    return answer