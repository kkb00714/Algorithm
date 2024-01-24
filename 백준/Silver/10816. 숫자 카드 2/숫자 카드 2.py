def search(arr, target, lt, rt):
    if lt > rt:
        return 0

    mid = (lt + rt) // 2
    if arr[mid] == target:
        return cnt.get(target)
        # cnt의 target을 반환
    elif arr[mid] < target:
        return search(arr, target, mid + 1, rt)
    else:
        return search(arr, target, lt, mid - 1)

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

cnt = {}
# 각 값이 몇 번 나타나는지 저장

for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in nums:
    print(search(cards, i, 0, len(cards)-1), end=' ')
# nums 리스트를 순회하면서 search 함수를 호출