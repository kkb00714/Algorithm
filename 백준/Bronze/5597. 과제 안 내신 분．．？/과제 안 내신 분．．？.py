student = list(range(1, 31))

for _ in range(28):
    a = int(input())
    student.remove(a)

for x in student:
    print(x)