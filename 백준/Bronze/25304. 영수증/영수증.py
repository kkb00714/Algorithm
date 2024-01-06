x = int(input())
n = int(input())
cnt = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    cnt += a * b

if cnt == x:
    print('Yes')
else:
    print('No')

