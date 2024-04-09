n = int(input())
m = int(input())

d = []

for num in range(n, m+1): 
    cnt = 0 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0: 
                cnt += 1 
                break
        if cnt == 0: 
            d.append(num)

if len(d) > 0:
    print(sum(d))
    print(min(d))
else:
    print(-1)
