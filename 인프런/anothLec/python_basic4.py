# 4. 반복문(for, while, break, continue)
# range는 순차적으로 정수 리스트를 만드는 함수

# a = range(10)
# print(list(a))

# a = range(1, 10)
# print(list(a))

# for i in range(10):
#     print("hello")

# for i in range(1, 10, 2):
#     print(i)

# for j in range(10, 0, -2):
#     print(j)



# while문

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
    
# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1
    
# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break
#     i = i + 1
    
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue # i가 짝수일 때, 모든 for문에 속해있는 구문들은 무시되고 지나감
        
#     print(i)
#     print(i + 2)
    

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)
    
# for else => for문이 정상종료가 된다면 else에 있는 것도 실행
# 만약 중간에 break가 됐다면 else는 실행하지 않음






