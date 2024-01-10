n = int(input())
a = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(n):
    if a[i] == v:
        cnt += 1

print(cnt)
