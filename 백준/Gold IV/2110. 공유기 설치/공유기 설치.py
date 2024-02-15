n, c = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))
a.sort()

def home(len):
    cnt = 1
    end = a[0]
    for i in range(1, n):
        if a[i] - end >= len:
            # 다음 집 - 마지막 집 >= 목표 길이
            cnt += 1
            end = a[i]
    return cnt

lt, rt = 1, a[n - 1]

while lt <= rt:
    mid = (lt + rt) // 2
    if home(mid) >= c:
        wifi = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(wifi)