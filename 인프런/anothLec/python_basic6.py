# 7. 문자열과 내장함수

msg = "It is Time"

print(msg.lower()) # 소문자
print(msg.upper()) # 대문자
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find('T')) 
# 문자열 하나하나가 리스트에 존재 (tmp[0] = I)
# find 함수는 문자열이 어느 인덱스에 있는지 찾아줌

print(tmp.count('T'))
# tmp 에서 T가 몇 개 있는지 세어주는 함수

print(msg[:2])
# 문자열 제일 처음부터, 인덱스 1번까지 출력함 (리스트 슬라이스)

print(msg[3:5])
# 3번 인덱스부터 4번 인덱스까지 출력

print(len(msg))
# msg의 길이를 구해줌

for i in range(len(msg)):
    # i 는 0부터 9까지.
    print(msg[i], end=' ')
print()

for x in msg: # x가 msg의 문자 한 개 한 개를 차례차례 접근함
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): # 대문자인지 확인하는 함수
        print(x, end=' ')
print()    

for x in msg:
    if x.islower(): # 소문자인지 확인하는 함수
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳만 출력
        print(x, end=' ')
print()

tmp = 'AZ'
for x in tmp:
    print(x,' : ', ord(x)) # 아스키코드로 출력
    # Tip! 아스키코드) A(65) ~ Z(90)
print()

tmp = 'az'
for x in tmp:
    print(x,' : ', ord(x)) 
    # Tip! 아스키코드) a(97) ~ z(122)
print()

tmp = 65
print(chr(tmp)) # 아스키코드에 대응되는 알파벳(문자)을 출력

