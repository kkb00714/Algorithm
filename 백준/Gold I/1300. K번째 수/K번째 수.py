n = int(input())
k = int(input())

# k 번째 수가 존재 => k보다 작거나 같은 수가 k개 존재
# mid(가운데 값)를 지정해서 이분 탐색 진행

lt, rt = 0, k

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0

    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt >= k:
        result = mid
        rt = mid - 1
    else:
        lt = mid +  1

print(result)