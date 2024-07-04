n = int(input())
# 3kg / 5kg 봉투

cnt = 0

while n >= 0:
    if n % 5 == 0: # 나누어 떨어지는 경우
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
