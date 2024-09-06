n = int(input())
seats = input()

cnt = seats.count('LL')
if  cnt <= 1:
    print(n)
else:
    print(n + 1 - cnt)
