n = int(input())
local = list(map(int, input().split()))
total = int(input())

lt = 0
rt = max(local)
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    money = 0
    for x in local:
        if x > mid:
            money += mid
        else:
            money += x

    if money <= total:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)
