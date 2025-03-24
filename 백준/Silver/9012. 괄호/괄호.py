def check_vps(arr):
    cnt = []
    
    for x in arr:
        if x == '(':
            cnt.append(x)
        elif x == ')':
            if cnt:
                cnt.pop()
            else:
                answer.append("NO")
                return
    
    if not cnt:
        answer.append("YES")
    else:
        answer.append("NO")


n = int(input())
answer = []

for i in range(n):
    arr = input().strip()
    check_vps(arr)

print(*answer, sep='\n')