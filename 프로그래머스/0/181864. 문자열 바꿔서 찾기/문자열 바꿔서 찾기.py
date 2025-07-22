def solution(myString, pat):
    result = myString.translate(str.maketrans('AB', 'BA'))
    return 1 if pat in result else 0

# str.maketrans('ABC', 'XYZ')
# => "A" → "X", "B" → "Y", "C" → "Z" 로 동시에 바꿀 수 있는 메서드
