# 9. 2차원 리스트 생성과 접근

# 1차원 리스트 생성
# a = [0] * 5 
# # n개의 리스트 값이 생성 (값은 0으로 동일함)
# print(a)

# 2차원 리스트 생성

a = [[0] * 3 for _ in range(3)]
# for _ 는 변수 없이 반복문만 반복함
# => 반복문이 세 번 반복하면서 1차원 리스트를 세 번 만들게 됨
print(a)

a[0][0] = 1
a[1][1] = 2
a[2][2] = 3
print(a)

for x in a:
    # a의 행에 차례차례 접근
    print(a)
print()

for x in a:
    for y in x: 
        # j가 x의 리스트의 원솟값에 하나하나 접근
        print(y, end=' ')
    print()






