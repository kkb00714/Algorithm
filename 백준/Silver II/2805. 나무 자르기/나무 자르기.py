def cut(trees, height):
    length = 0
    for tree in trees:
        if tree > height:
            length += tree - height
    return length

def search(trees, target_length):
    lt, rt = 0, max(trees)
    result = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        length = cut(trees, mid)

        # m 보다 나무의 길이가 크거나 같은 경우
        if length >= target_length:
            result = mid
            lt = mid + 1
        # m 보다 가져간 나무의 길이가 작은 경우
        else:
            rt = mid - 1
            
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

max_height = search(trees, m)
print(max_height)