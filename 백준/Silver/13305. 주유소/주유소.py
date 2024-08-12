n = int(input())
km = list(map(int, input().split()))
leter = list(map(int, input().split()))

cnt = 0 # 최소 비용
min_cnt = leter[0] # 처음 도시에 있는 기름값 

for i in range(n - 1):
    # 현재 도시의 기름값이 더 싸다면, min_cnt에 재할당
    if leter[i] < min_cnt:
        min_cnt = leter[i]

    cnt += min_cnt * km[i]

print(cnt)
