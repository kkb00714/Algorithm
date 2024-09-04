n = int(input())
drink = list(map(int, input().split()))

result = max(drink)
drink.remove(result)

for x in drink:
    result += x / 2
print(result)