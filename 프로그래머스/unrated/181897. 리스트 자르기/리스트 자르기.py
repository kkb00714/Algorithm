def solution(n, slicer, num_list):
    answer = []
    
    # n 에는 정수가 3개
    # slicer에 담긴 정수를 차례대로 a, b, c
    # => 정수들이 slicer에 들어갔단 뜻??? 문제가 왜이래
    # n에 따른 num_list 슬라이싱 하기
    
    a, b, c = slicer
    
    if n == 1:
        answer = num_list[0 : b + 1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a: b + 1]
    else:
        answer = num_list[a : b + 1 : c]
    
    return answer