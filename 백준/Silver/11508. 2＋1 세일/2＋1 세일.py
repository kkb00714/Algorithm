n = int(input())
goods = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for i in range(n):
    if i % 3 != 2:
        cnt += goods[i]

print(cnt)
