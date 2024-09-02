def cnt(N, K, sensors):
    if K >= N:
        return 0

    sensors.sort()
    
    distances = []
    for i in range(1, N):
        distances.append(sensors[i] - sensors[i - 1])
    
    distances.sort(reverse=True)
    
    return sum(distances[K-1:])

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

print(cnt(N, K, sensors))
