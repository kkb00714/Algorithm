n, m = map(int, input().split())
a = []
b = []

for _ in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

x = min(a)
y = min(b)

cnt = min((n // 6) * x + (n % 6) * y, (n // 6 + 1) * x, n * y)
print(cnt)
