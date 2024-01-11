n, m = map(int, input().split())
bsk = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    cnt = bsk[a-1 : b]
    cnt.reverse()
    bsk[a-1 : b] = cnt
    
for x in bsk:
    print(x, end =' ')