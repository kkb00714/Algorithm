n = int(input())
money = []

coins = [25, 10, 5, 1]

for _ in range(n):
    money = int(input())
    res = 0
    cnt = []
    while money != 0:
        for i in range(4):
            cnt.append(money // coins[i])
            money = money % coins[i]
    for x in cnt:
        print(x, end = " ")
    print()
