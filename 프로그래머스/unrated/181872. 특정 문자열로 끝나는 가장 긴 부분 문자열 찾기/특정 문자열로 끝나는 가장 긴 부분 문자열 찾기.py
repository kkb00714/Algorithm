def solution(myString, pat):
    answer = ''
    
    if pat in myString:
        
        end_index = myString.rindex(pat) + len(pat)
        # rindex(pat) : 특정 문자열에서, pat의 가장 오른쪽 위치를 반환하는 메서드
        
        answer = myString[:end_index]
    
    return answer