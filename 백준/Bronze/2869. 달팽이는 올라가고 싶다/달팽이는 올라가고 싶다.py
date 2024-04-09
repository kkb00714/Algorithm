a, b, v = map(int, input().split())

if (v - b) % (a - b) == 0:
    # 나머지가 0일 때 (다 올라갔을 때)
    print((v - b) // (a - b))
else:
    # 나머지가 0이 아닐 때 (다 올라가고 남았을 때 (?))
    print(((v - b) // (a - b)) + 1)
