num = int(input())
cnt = 1

while num > cnt:
    num -= cnt
    cnt += 1
    
if cnt % 2 == 0:
    a = num
    b = cnt - num + 1

elif cnt % 2 == 1:
    a = cnt - num + 1
    b = num

print(f'{a}/{b}')
