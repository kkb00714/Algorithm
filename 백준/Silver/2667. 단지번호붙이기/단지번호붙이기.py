def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 이미 방문했거나 단지의 끝인 경우
    if maps[x][y] == 0:
        return False

    # 방문 처리
    maps[x][y] = 0
    cnt = 1

    cnt += dfs(x + 1, y)
    cnt += dfs(x - 1, y)
    cnt += dfs(x, y - 1)
    cnt += dfs(x, y + 1)

    # 탐색 종료 후 해당 단지의 집 개수 반환
    return cnt

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]

arr = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            arr.append(dfs(i, j))

print(len(arr))
for i in sorted(arr):
    print(i)
