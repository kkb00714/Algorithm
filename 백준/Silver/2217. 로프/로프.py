n = int(input())
ropes = []
total = cnt = 0
for i in range(n):
    ropes.append(int(input()))
    total += ropes[i] # 
ropes.sort()

for i in range(n):
    cnt = max(cnt, ropes[i] * (n - i))
print(cnt)