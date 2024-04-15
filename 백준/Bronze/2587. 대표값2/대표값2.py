a = []
ave = 0
for _ in range(5):
    n = int(input())
    a.append(n)
    ave += n
a.sort()
print(ave//5)
print(a[2])