'''
반복문을 이용한 문제풀이
1. 1부터 N까지 홀수출력하기
2. 1부터 N까지의 합 구하기
3. N의 약수 출력하기
'''

n = int(input())

# 1
for i in range(1, n + 1):
    if i % 2 == 1:
        print("홀수: ", i)
        
# 2
sum = 0
for i in range(1, n + 1):
    sum = sum + i
    print(sum)
print("최종 합 : " ,sum)

# 3
for i in range(1, n + 1):
    if n % i == 0: # n을 i로 나누었을 때 나머지가 0인 경우
        print("약수: ", i, end=" ")


