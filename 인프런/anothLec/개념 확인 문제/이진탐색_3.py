# 파이썬 이진 탐색 라이브러리 

from bisect import bisect_left, bisect_right

# bisect_left(a, x) => 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) => " 가장 오른쪽 인덱스 반환

a = [1, 2, 5, 6, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


# 응용 - 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index

b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(b, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(b, -1, 3))