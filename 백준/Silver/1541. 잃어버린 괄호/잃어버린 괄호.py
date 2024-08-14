n = input().split('-')
cnt = 0
for i in range(len(n)):
    if '+' in n[i]:
        num = n[i].split('+')
        result = sum(map(int, num))
    else:
        result = int(n[i])
    if i == 0:
        cnt += result
    else:
        cnt -= result
print(cnt)