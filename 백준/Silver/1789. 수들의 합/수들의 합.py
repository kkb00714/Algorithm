n = int(input())
cnt = 0
result = 0

while True:
    cnt += 1
    result += cnt
    if result > n:
        break
print(cnt-1)
