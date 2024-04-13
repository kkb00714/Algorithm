n, m = map(int, input().split())
cards = list(map(int, input().split()))
cnt = 0 # 이전 값을 넣을 변수

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j+1, n):
            result = cards[i] + cards[j] + cards[k]
            if(result <= m and result > cnt):
                cnt = result
print(cnt)