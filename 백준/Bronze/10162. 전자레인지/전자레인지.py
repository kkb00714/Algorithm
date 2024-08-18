n = int(input())
btn = [300, 60, 10]
result = []

for time in btn:
    result.append(n // time)
    n %= time

if n != 0:
    print(-1)
else:
    for x in result:
        print(x, end=' ')