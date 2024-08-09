# 선택 정렬
# 선택정렬 알고리즘을 사용하여 리스트 안의 자료를 순서대로 배열하기

# 입력예시
# 35 9 2 85 17

# 출력
# 2, 9, 17, 35, 85


arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)
