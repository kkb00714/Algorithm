def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk: 
        # stk 가 비어있으면 True를 반환 = 아래 코드 실행
            stk.append(arr[i])
            i += 1
            
        elif stk and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
            
        elif stk and stk[-1] >= arr[i]:
            stk.pop()
            
    return stk