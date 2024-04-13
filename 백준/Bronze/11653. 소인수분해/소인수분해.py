def decimal(x):
    cnt = []
    res = 2
    while x > 1:
        while x % res == 0:
            cnt.append(res)
            x //= res
        res += 1
    return cnt

n = int(input())
result = decimal(n)
for x in result:
    print(x)
