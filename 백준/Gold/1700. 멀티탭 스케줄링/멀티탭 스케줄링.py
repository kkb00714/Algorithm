n, cnt = map(int, input().split())
e = list(map(int, input().split()))

result = []
num = 0

for i in range(cnt):
    if e[i] in result:
        continue
    
    if len(result) < n:
        result.append(e[i])
        
    else:
        # 현재 멀티탭에 꽂힌 기기 중 다음으로 가장 늦게 사용될 기기를 찾아 뽑기
        future_positions = {}
        for device in result:
            # 해당 기기가 다음에 언제 사용되는지 찾음 아오증말로다가
            try:
                future_positions[device] = e[i+1:].index(device)
            except ValueError:
                # 더 이상 사용되지 않는 경우, 가장 우선적으로 제거
                future_positions[device] = float('inf')

        # 가장 늦게 다시 사용되는 기기를 뽑음
        to_unplug = max(future_positions, key=future_positions.get)
        result.remove(to_unplug)
        result.append(e[i])
        num += 1

print(num)