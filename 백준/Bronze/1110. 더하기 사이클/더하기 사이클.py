n = int(input())
num = n
cnt = 0

while True:
    cnt += 1

    a = n // 10
    b = n % 10

    result = b * 10 + (a + b) % 10
    if result == num:
        break
    n = result
print(cnt)
