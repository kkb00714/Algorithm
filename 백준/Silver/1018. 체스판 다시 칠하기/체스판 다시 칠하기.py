n, m = map(int, input().split())

# board에 체스판의 상태를 저장하고, result 리스트를 다시 칠해야 하는 정사각형 수를 저장
board = []
result = []

# n개의 줄에 걸쳐 각 행을 입력받은 후 board에 추가

for _ in range(n):
    board.append(input())

# n * m 크기의 모든 체스판을 확인
for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0

        # 현재 위치의 인덱스의 홀/짝 구분 후
        # 번갈아서 칠해질 수 있도록 구분
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1

        # 다시 칠해야하는 정사각형 수를 result에 추가
        result.append(draw1)
        result.append(draw2)

# 리스트에서 최솟값을 출력 (최초로 다시 칠해야 하는 정사각형의 수를 의미)
print(min(result))