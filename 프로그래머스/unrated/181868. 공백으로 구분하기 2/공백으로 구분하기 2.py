import re

def solution(my_string):
    my_string = my_string.strip()
    answer = re.split(r'\s+', my_string)
    
    # re.split() 함수는 정규 표현식 r'\s+'를 사용하여 문자열을 분리
    # 이 정규 표현식은 하나 이상의 공백 문자(스페이스, 탭, 개행 등)를 나타내므로
    # 연속되는 공백도 하나의 공백으로 처리 가능함
    
    return answer