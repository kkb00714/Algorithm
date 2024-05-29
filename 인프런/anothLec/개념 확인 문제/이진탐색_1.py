# 이미 정렬된 10개의 데이터 중 값이 4인 원소를 찾는 예시 (함수 활용)

# 리스트 
# 0 2 4 6 8 10 12 14 16 18

def binary_search (array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점이 target 값보다 크다면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점이 target 값보다 작다면 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

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