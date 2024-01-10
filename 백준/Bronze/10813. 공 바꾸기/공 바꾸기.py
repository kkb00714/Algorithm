n, m = map(int, input().split())
bsk = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    cnt = bsk[i-1] # 첫번째 박스에 있던 공의 번호를 cnt에 할당
    bsk[i-1]=bsk[j-1] # 두번째 박스에 담겨있던 공의 번호를 첫번째 박스에 할당
    bsk[j-1] = cnt # 두번째 박스에 첫번째 공의 번호를 할당

for b in bsk:
    print(b, end=' ')
