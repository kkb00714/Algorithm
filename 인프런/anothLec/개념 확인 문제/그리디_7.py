'''
시각 문제 

정수 N이 입력되면 00시 00분 00초부터 
N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램 작성

00시 00분 3초 => 세어야 하는 시각
01시 25분 22초 => 세면 안 되는 시각


입력 조건 : 첫째 줄에 정수 N이 입력(0 <= N <= 23)
출력 조건 : 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 출력
input : 
5
output:
11475

'''

# 내가 짠 코드

time = int(input())
cnt = 0

for i in range(time + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                cnt += 1
print(cnt)


# 해설 코드

h = int(input())
cnt = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or str(j) or str(k):
                cnt += 1
print(cnt)