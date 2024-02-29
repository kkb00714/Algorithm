n, k = map(int, input().split())

f = []
for i in range(1, n+1):
    if n % i == 0:
        f.append(i)
        
if len(f) < k:
    print(0)
else:
    print(f[k-1])