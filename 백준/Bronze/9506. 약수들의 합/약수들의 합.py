for _ in range(100000):
    n = int(input())
    if n == -1:
        break

    f = [1]
    for i in range(2, n//2 + 1):
        # 약수이므로 절반까지만 검사해도 충분!
        if n % i == 0:
            f.append(i)

    if sum(f) == n:
        print(f"{n} = {' + '.join(map(str, f))}")
    else:
        print(f"{n} is NOT perfect.")