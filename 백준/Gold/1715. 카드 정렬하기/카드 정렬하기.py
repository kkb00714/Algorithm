import heapq

n = int(input())
a = []

for _ in range(n):
    heapq.heappush(a, int(input()))

result = 0

while len(a) > 1:
    first = heapq.heappop(a)
    second = heapq.heappop(a)

    cnt = first + second
    result += cnt

    heapq.heappush(a, cnt)

print(result)
