# 떡볶이 떡 만들기 => 과제! (5/30 까지)

# 절단기에 높이 H를 지정하면 줄지어진 떡을 한번에 절단함.
# 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고,
# 낮은 떡은 잘리지 않음.

# 예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고
# 절단기 높이를 15cm로 지정하면
# 다른 뒤의 떡의 높이는 15, 14, 10, 15cm가 된다.
# 잘린 떡의 길이는 차례대로 4, 0, 0, 2이다. 따라서 손님은 6cm 만큼의 길이를 가져감.

# 손님이 왔을 때 요청한 총 길이가 M일 때,
# 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값은?


# 풀이
# input
# 19 14 10 17
# 6 (받을 떡의 길이를 6cm 로 가정)

# output
# 4


        
array = list(map(int, input().split()))
a = int(input())
lt = 0
rt = max(array)
cnt = 0
while lt <= rt:
    result = 0
    mid = (lt + rt) // 2
    for x in array:
        # 떡을 잘랐을 때의 떡의 양 계산
        if x > mid:
            result += x - mid
    # 떡의 양이 부족한 경우 왼쪽으로
    if result < a:
        rt = mid - 1
    # 떡의 양이 많은 경우 오른쪽으로
    else:
        cnt = mid
        lt = mid + 1
print(result)