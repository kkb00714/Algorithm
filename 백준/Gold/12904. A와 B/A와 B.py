s = input()
t = input()

# 문자열 t가 s와 같아질 때까지 빼면서 진행
while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
        
    elif t[-1] == 'B':
        t = t[:-1][::-1]
        # t[:-1] : 끝에서 첫 번째 문자를 제외한 나머지 부분을 가져옴
        # t[::-1] : 문자열을 뒤집는 슬라이싱 기법

if t == s:
    print(1)
else:
    print(0)