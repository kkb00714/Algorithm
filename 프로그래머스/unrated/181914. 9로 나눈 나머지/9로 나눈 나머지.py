def solution(number):
    
    # 새로운 사실!) 음이 아닌 정수 // 9 == 각 자리 숫자의 합 % 9
    
    # < 실패했지만 어려웠던 코드 >
    # num = [int(digit) for digit in number]
    # 문자열 number의 각 문자('digit') 을 순회하면서
    # 각 문자를 정수로 변환한 뒤, 새로운 리스트 num에 저장함
    
    # for digit in number => number 의 문자열의 각 문자를 하나씩 반복적으로 가져옴
    # int(digit) => number의 문자들이 들어있는 digit을 정수로 변환함

    num_str = str(number) 
    # 숫자를 문자열로 변환
    num_list = [int(digit) for digit in num_str]
    # 변환한 문자열을 정수로 변환하여 리스트에 저장
    total = sum(num_list)
    # 리스트에 있는 숫자들의 합
    answer = total % 9
    # 합을 9로 나눈 나머지

    return answer