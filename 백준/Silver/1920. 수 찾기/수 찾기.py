def search(t, a):
    lt, rt = 0, len(a) - 1 

    while lt <= rt :
        mid = (lt + rt ) // 2

        if a[mid] == t:
            return True
        elif a[mid] < t: 
            lt = mid + 1
        else:
            rt = mid - 1
    return False

n = int(input())
na = sorted(list(map(int, input().split())))
m = int(input())
ma = list(map(int, input().split()))

for i in ma:
    if search(i, na):
        print(1)
    else:
        print(0)