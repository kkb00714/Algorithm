n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
cnt = 0

for i in range(n):
    cnt += a[i] * max(b)
    b.remove(max(b))
print(cnt)
