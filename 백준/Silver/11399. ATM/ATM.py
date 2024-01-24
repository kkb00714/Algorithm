n = int(input())
wait = list(map(int, input().split()))
wait.sort()

res = cnt = 0
for i in range(len(wait)):
    res = wait[i] + res
    cnt += res
print(cnt)