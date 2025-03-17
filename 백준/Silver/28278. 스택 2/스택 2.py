import sys

n = int(sys.stdin.readline().strip())
stack = []
output = []

for _ in range(n):
    cnt = sys.stdin.readline().split()  
    
    if cnt[0] == '1':
        stack.append(cnt[1])

    elif cnt[0] == '2':
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append("-1")

    elif cnt[0] == '3':
        output.append(str(len(stack)))

    elif cnt[0] == '4':
        output.append("0" if stack else "1")

    elif cnt[0] == '5':
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append("-1")

sys.stdout.write("\n".join(output) + "\n")