n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

cnt = 0
for i in array:
    cnt += i.count(1)
print(cnt)