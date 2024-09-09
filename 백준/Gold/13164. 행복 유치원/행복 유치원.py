n, group = map(int, input().split())
kids = list(map(int, input().split()))
kids.sort()

cnt = []

for i in range(1, n):
    cnt.append(kids[i] - kids[i-1])
    
cnt.sort(reverse=True)
print(sum(cnt[group-1:]))
