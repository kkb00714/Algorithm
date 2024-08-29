n = int(input())
archer = list(map(int, input().split()))

hanzo = 0 
kill = 0
result = []


for x in archer: 
    if x > hanzo:
        result.append(kill)
        hanzo = x
        kill = 0
    else:
        kill += 1
        
result.append(kill)

print(max(result))
