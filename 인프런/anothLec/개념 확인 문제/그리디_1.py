# 거스름돈 거슬러 주기 
# 1, 5, 10, 50, 100, 500 (거스름돈) 존재
# 거슬러주어야 할 금액 230원
# 최소한의 동전으로 거슬러줄 때, 그 개수

coins = list(map(int, input().split()))
change = int(input())
coins.sort(reverse=True)

cnt = 0

for x in coins:
    while change >= x:
        # 받아야 할 거스름돈이 현재 동전금액 보다 크다면
        change -= x 
        # 거스름돈 - 현재 동전(금액)
        cnt += 1
print(cnt)
    


