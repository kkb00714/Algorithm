# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행.
# 1. N에서 1을 뺌.
# 2. N을 K로 나눔.

# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의
# 과정을 수행해야 하는 최소 횟수를 작성

# input
# N : 17 / K : 4

n, k = map(int, input().split())
cnt = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    cnt += (n - target)
    n = target

    # n이 k보다 작을 때 break 
    if n < k:
        break
    
    # k로 나눔
    cnt += 1
    n //= k
    
# 마지막으로 남은 수에서 1을 뺌
cnt += (n - 1)
print(cnt)
