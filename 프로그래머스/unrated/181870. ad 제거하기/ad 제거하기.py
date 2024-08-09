def solution(strArr):
    answer = [s for s in strArr if 'ad' not in s]
    # 리스트 컴프리헨션
    # 여기서 s 는 각 리스트의 요소인 문자열을 의미
    # for s in strArr => strArr 리스트를 순회하며 각 요소를 's'에 대입함        
    # if 'ad' no in s => 부분문자열 'ad'가 문자열 's' 에 없을 경우, 해당 문자열을 선택함 
    
    return answer
