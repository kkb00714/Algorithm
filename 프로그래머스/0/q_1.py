# 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. 
# myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 
# pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

def solution(myString, pat):
    result = myString.translate(str.maketrans('AB', 'BA'))
    return 1 if pat in result else 0

# str.maketrans('ABC', 'XYZ')
# => "A" → "X", "B" → "Y", "C" → "Z" 로 동시에 바꿀 수 있는 메서드
