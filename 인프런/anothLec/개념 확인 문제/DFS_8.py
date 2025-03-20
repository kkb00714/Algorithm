# 인프런 DFS 문제 4

# 바둑이 승차
# 철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 
# 그런데 그의 트럭은 C킬로그램 넘게 태울 수가 없다. 
# 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 
# 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하세요.

# 입력 설명
# 첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
# 둘째 줄부터 N마리 바둑이의 무게가 주어진다.

# 출력 설명
# 첫 번째 줄에 가장 무거운 무게를 출력한다.

# 입력
# 259 5
# 81
# 58
# 42
# 33
# 61

# 출력
# 242

# 트럭 제한 무게 259kg, 바둑이 5마리

def dfs(idx, cnt):
    global answer
    if cnt > c:
        return False
    
    if idx == n:
        if cnt > answer:
            answer = cnt
    else: 
        dfs(idx + 1, cnt + weight[idx])
        dfs(idx + 1, cnt)

c, n = map(int, input().split())
weight = []
answer = 0

for i in range(n):
    weight.append(int(input()))
print(weight)
dfs(0, 0)
print(answer)