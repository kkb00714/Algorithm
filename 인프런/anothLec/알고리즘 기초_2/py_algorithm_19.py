# 19. 봉우리

# 문제
# 지도 정보가 N*N 격자판에 주어집니다. 
# 각 격자에는 그 지역의 높이가 쓰여있습니다. 
# 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 
# 큰 숫자는 봉우리 지역입니다. 

# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 
# 봉우리의 개수는 10개입니다.


# 입력 설명 
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 
# N개의 자연수가 주어진다. 
# 각 자연수는 100을 넘지 않는다. 

# 출력 설명
# 봉우리의 개수를 출력하세요.

# 입력 예제
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

# 출력 예제
# 10


dx = [-1, 0, 1, 0] 
dy = [0, 1, 0 ,-1]
# 상하좌우를 탐색하기 위해 미리 초기화를 해놓음

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n) # 0번 인덱스에 0으로 초기화된 리스트를 삽입
a.append([0] * n) # 마지막 인덱스에 0으로 초기화된 리스트를 삽입

for x in a:
    x.insert(0, 0) # 각 행의 앞에 0을 삽입
    x.append(0) # 각 행의 마지막 인덱스에 0삽입
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
        # 모든 조건이 참일 때 시행
            cnt += 1    

print(cnt)




