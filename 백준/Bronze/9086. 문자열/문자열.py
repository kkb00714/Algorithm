n = int(input())
arr = []
for _ in range(n):
    s = str(input())
    cnt = s[0]+s[-1]
    arr.append(cnt)

for x in arr:
    print(x)