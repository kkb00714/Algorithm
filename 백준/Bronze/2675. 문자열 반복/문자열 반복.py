t = int(input())
for _ in range(t):
    arr = []
    r, s = input().split()
    for i in range(len(s)):
        arr += (s[i]) * int(r)
        arr = ''.join(arr)
    print(arr)