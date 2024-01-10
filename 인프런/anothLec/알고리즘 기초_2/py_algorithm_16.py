# 16. 격자판 최대합

# 문제
# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 
# 가장 큰 합을 출력합니다.

# 입력 설명 
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 각 자연수는 100을 넘지 않는다. 

# 출력 설명
# 최대합을 출력합니다.

# 입력 예제
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# 출력 예제
# 155


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# map을 통해서 한 줄을 읽음
# 변수없이 for문으로 n번 반복함

largest = -2147000000 # 가장 작은 값으로 초기화
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 가로의 합
        sum2 += a[j][i] # 세로의 합

    if sum1 > largest:
        largest = sum1

    if sum2 > largest:
        largest = sum2

sum1 = sum2= 0
for i in range(n):
    sum1 += a[i][i] # 우하향 대각선의 합
    sum2 += a[i][n-i-1] # 좌하향 대각선의 합

if sum1 > largest:
    largest = sum1

if sum2 > largest:
    largest = sum2

print(largest)

    

