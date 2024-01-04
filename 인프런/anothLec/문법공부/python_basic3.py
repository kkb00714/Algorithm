# 3. 조건문(if 분기문, 다중if문)

# if문

x = 1
if x == 1:
    print("x는 1입니다.")

z = 15
if z >= 0:
    if z % 2 == 1:
        print("x는 홀수입니다.")
    if z % 2 == 0:
        print("x는 짝수입니다.")

# 분기문
x = 7
if x > 0:
    print("양수")
else:
    print("음수")

# 다중 if문
y = 93
if y >= 90:
    print('A')
elif y >= 80:
    print('B')
elif y>= 70:
    print("C")
else:
    print("F")