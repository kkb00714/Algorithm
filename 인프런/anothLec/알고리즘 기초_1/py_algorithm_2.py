# 2. K번째 수

# 문제
# >> N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서
# >> s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 
# >> k번째로 나타나는 숫자를 출력

# 입력 설명
# >> 첫 번째 줄에 테스트 케이스 T(1 <= T <= 10)이 주어집니다.
# >> 각 케이스별 첫 번째 줄은 자연수 (5 <= N <= 500), s, e, k 가 차례로 주어집니다.
# >> 두 번째 줄에 N개의 숫자가 차례로 주어진다.

# 출력 설명
# >> 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하시오.
# >> 

# 입력 예제
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15 

# 출력 예제
# 1 7
# 2 6


T = int(input()) # 케이스 개수
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e] # s번째부터 e번째까지 (인덱스 번호로 변환)
    # 마지막 인덱스는 포함이 안 되니까 e => e-1을 의미하게 됨
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
    