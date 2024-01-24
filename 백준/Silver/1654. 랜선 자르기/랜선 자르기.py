def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
Line = []
nums = 0
largest = 0
for i in range(k):
    line = int(input())
    Line.append(line)
    largest = max(line, largest)

lt, rt = 1, largest

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        nums = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(nums)