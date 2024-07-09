# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 각 노드와 인접한 노드들을 작성
graph = [
    [], 
    # 첫번째 인덱스는 0 으로 이용하는 것이 헷갈리지 않고 직관적일 수 있다!
    [2, 3, 8], # 1번 노드와 인접한 노드인 2 3 8
    [1, 7], # 2번 노드와 " 1 7
    [1, 4, 5], # 3번 노드와 ...
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] # 마지막 8번 노드와 인접한 1, 7
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)