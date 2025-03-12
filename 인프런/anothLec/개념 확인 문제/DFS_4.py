# 문제4 - GPT
# N x M 크기의 미로가 주어질 때, 
# (0,0)에서 (N,M)까지 이동할 수 있는지 DFS로 판별하라. 
# 이동은 상하좌우로만 가능하며, 
# 0은 이동 가능, 1은 벽을 의미한다.

# 입력 예시 (원래는 숫자만)
# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0]
# ]

# 출력 예시
# YES

def dfs_maze(x, y):
    # 출구에 도달한 경우
    if x == len(maze) - 1 and y == len(maze) - 1:
        return True
    
    # 미로의 범위를 벗어나면 종료
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze):
        return False
    
    # 벽이거나 이미 방문한 곳이라면 종료, 아니라면 방문 처리
    if maze[x][y] == 1 or visited[x][y]:
        return False
    
    # 현재 위치 방문 처리
    visited[x][y] = True
    # print(f"({x}, {y}) 방문")
        
    # 상, 좌, 하, 우 순서로 탐색 진행
    if (dfs_maze(x - 1, y) or
        dfs_maze(x, y - 1) or
        dfs_maze(x + 1, y) or
        dfs_maze(x, y + 1)):
        return True
    
    return False

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# 방문 여부를 저장하는 이유
# 방문 처리를 1로 변경해버리면 미로를 다시 사용해야 할 때 변경되어 버리기 때문.
visited = [[False] * 5 for _ in range(5)]

if dfs_maze(0, 0):
    print("YES")
else:
    print("NO")
