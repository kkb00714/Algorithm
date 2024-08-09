def solution(l, r):
    answer = []
    nums = False
    
    # 정수 l, r 이 주어졌을 때, l 이상 r 이하의 정수 중, 숫자 0, 5 으로만 이루어진 모든 정수를 오름차순으로 배열하기

    for i in range(l, r + 1):
        if all(digit in {'0', '5'} for digit in str(i)):
        # for digit in str(i) => 정수 i를 문자열로 변환 후 
        # 그 문자열을 순환하면서 각 문자를 digit 변수에 할당함
        
        # all~ => digit 가 0 또는 5와 일치하는지 확인함.
        # digit 가 모든 문자에 대해 0 또는 5와 일치한다면
        # all 함수는 True 를 반환하고, 그렇지 않으면 False를 반환
            answer.append(i)
            nums = True
                
    if not nums:
        answer.append(-1)


    return answer