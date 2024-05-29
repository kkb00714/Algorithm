# 이진  탐색 소스코드 구현 (반복문 구현)



def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 중간점보다 찾고자 하는 값이 작은 경우
        elif array[mid] > target:
            end = mid - 1
        # 중간점보다 찾고자 하는 값이 큰 경우
        else:
            start = mid + 1
    return None

# n (원소의 개수), target (찾고자 하는 값) 입력
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)