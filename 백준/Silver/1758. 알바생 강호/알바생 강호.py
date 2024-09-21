n = int(input())
tip = 0
customer = []

for _ in range(n):
    customer.append(int(input()))
customer.sort(reverse=True)

for i in range(n):
    result = customer[i]
    cnt = result - i
    if cnt > 0 :
        tip += cnt
                    
print(tip)