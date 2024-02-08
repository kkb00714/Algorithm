while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    if a < b and b % a == 0: # 약수일 경우
        print('factor')
    elif a > b and a % b == 0: # 배수일 경우
        print('multiple')
    else:
        print('neither')