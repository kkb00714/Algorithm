# 5. 정다면체

# 문제
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 
# 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 
# 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# 입력 설명
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. 
# N과 M은 4, 6, 8, 12, 20 중의 하나입니다

# 출력 설명
# 첫 번째 줄에 답을 출력합니다.

# 입력 예제
# 4 6

# 출력 예제
# 5 6 7


n, m = map(int, input().split())

cnt = [0]*(n+m+3) # 두 주사위의 눈의 합이 나오는 횟수를 나타냄

max_count = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
        
for i in range(n+m+1): # 두 눈의 합까지
    if cnt[i] >= max_count: 
        # cnt[i]의 값이 최댓값보다 클 때
        max_count = cnt[i] 
        # max에 현재 cnt[i] 값을 덮어씀
        
for i in range(n+m+1):
    if cnt[i] == max_count: 
        # 두 주사위의 눈의 합이 max와 같은 경우 
        # (max 값이 여러개인 경우 출력) 
        print(i, end=' ')

