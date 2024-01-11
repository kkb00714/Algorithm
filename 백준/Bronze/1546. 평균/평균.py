n = int(input())
m = list(map(int, input().split()))
score = max(m)

cnt = 0
for i in range(n):
    cnt += m[i] / score  *100
print(cnt / n)