n, k = map(int, input().split())
money = []
for i in range(n):
    nums = int(input())
    money.append(nums)

money.sort(reverse=True)

answer = 0
for coin in money:
    if k >= coin: # 만들어야 할 값보다 돈이 더 작다면
        answer += k // coin
        # 몫 만큼 더하기
        k %= coin
        # 나머지 값을 k에 재할당
        if k <= 0:
            break
print(answer)