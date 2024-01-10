n, m = map(int, input().split())
lst = [0] *( n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a부터 b까지 c번 넣음
    for i in range(a, b+1):
        lst[i] = c
        
for i in range(1, n+1):
    print(lst[i], end=' ')
