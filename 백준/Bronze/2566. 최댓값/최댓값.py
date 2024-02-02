A = []
m = 0
lt = rt = 0
for i in range(9):
    a = list(map(int, input().split()))
    A.append(a)
    
for i in range(9):
    for j in range(9):
        if A[i][j] >= m:
            m = A[i][j]
            lt, rt = i + 1, j + 1
print(m)
print(lt, rt)