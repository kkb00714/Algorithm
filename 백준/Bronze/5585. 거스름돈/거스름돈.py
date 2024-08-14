n = int(input())
change = [500, 100, 50, 10, 5, 1]
n = 1000 - n
cnt =  0
for i in range(len(change)):
        result = n
        n = n % change[i]
        cnt += result // change[i]
print(cnt)