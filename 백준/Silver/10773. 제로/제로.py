n = int(input())
nums = []

for _ in range(n):
    x = int(input())
    if x == 0:
        nums.pop()
    else:
        nums.append(x)
print(sum(nums))
