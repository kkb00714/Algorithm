# 쇠 막대기 

# 문제
'''

너무 길어서 스킵

'''


# 입력 설명 
# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 
# 괄호 문자의 개수는 최대 100,000이다. 

# 출력 설명
# 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.

# 입력 예제
# ()(((()())(())()))(())

# 출력 예제
# 17


s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        # 레이저일 때 
        if s[i-1] == '(': 
            stack.pop()
            cnt += len(stack) 
            # stack의 길이를 누적 (쇠박대기의 갯수)
            
        # 레이저가 끝났을 때
        else:
            # 쇠막대기의 끝이므로, 잘린 것을 +1 함
            stack.pop()
            cnt += 1
print(cnt)



