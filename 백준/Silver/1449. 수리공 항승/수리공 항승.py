def min_tape_count(N, L, leaks):
    leaks.sort()
    cnt = 0
    end = 0

    for x in leaks:
        # 만약 현재 테이프가 이 위치를 덮지 못한다면
        if x > end:
            # 새로운 테이프를 사용해야 하므로 개수를 증가시키고
            cnt += 1
            # 현재 위치부터 테이프가 덮을 수 있는 범위를 갱신
            end = x + L - 1

    return cnt

N, L = map(int, input().split())
leaks = list(map(int, input().split()))

print(min_tape_count(N, L, leaks))