h, m = map(int, input().split())
c = int(input())

h += c // 60
m += c % 60

if m >= 60: 
     h = h+1
     m = m - 60
if h >= 24:
    h -= 24

print(h, m)
    
