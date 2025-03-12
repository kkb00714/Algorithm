# 음료수 얼려 먹기
# N x M 크기의 얼음 틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시.
# 이 때, 얼음 틀의 모양이 주어졌을 때, 총 아이스크림의 개수는?
# 사진 자료의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됨.

# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력
# 3

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        
        # (현재 위치 기준) 상, 하, 좌, 우 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        
        return True
    return False

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    # 한 줄을 입력받고, 각 원소를 정수로 바꿔서 리스트로 변환
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 실행
        if dfs(i, j) == True:
            result += 1

print(result)