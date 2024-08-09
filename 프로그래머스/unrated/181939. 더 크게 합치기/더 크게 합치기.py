def solution(a, b):
    
    answer = int(max(f"{a}{b}", f"{b}{a}"))
    return answer
    # 두 개의 문자열 (ab, ba) 중에서 더 큰 값을 선택하여 answer에 할당 후 출력