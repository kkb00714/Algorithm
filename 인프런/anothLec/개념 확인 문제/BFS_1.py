from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
bfs(graph, 1, visited)