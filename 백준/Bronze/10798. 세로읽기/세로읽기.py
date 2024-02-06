a = []
for _ in range(5):
    a.append(list(input()))

for j in range(15):
    for i in range(5):
        if j < len(a[i]):
            # j가 행의 길이보다 작을 때만 그 문자들을 출력하도록 조건 
            print(a[i][j], end='')