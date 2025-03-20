# 인프런 DFS 문제 3

# 인프런 문제
# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하시오.
# 단, 재귀함수를 이용하여 출력해야 함.

# 입력
# 11

# 출력
# 1011

def dfs(n):
    if n == 0:
        return
    else:
        # 여기서 2진수 출력의 순서를 뒤집고 싶으면 
        # print문을 dfs 함수의 위로 올리면 됨.
        # print(n % 2, end='')
        
        dfs(n // 2)
        print(n % 2, end='')

n = int(input())
arr = []

dfs(n)