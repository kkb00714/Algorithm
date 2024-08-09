def solution(arr):
    answer = 0
    new_arr = arr
    
    while True:
        change = []
        # 새 배열 생성      
        for i in new_arr:
            # i 가 조건에 합당할 때 change에 각각 원소들을 저장
            if i >= 50 and i % 2 == 0:
                change.append(i // 2)
            elif i < 50 and i % 2 == 1:
                change.append(i * 2 + 1)
            else:
                change.append(i)
                
        same = all(a == b for a, b in zip(new_arr, change))
        # all 함수는 순회 가능한 객체의 모든 요소가 조건을 만족할 때,
        # True를 반환.
        
        # 여기서 두 배열을 순서대로 짝을 지어서 튜플 형태로 만들고,
        # 이 튜플들에 대해 a == b 조건을 확인함. 즉, 두 배열의 같은 위치에 있는 원소끼리 비교함
        # all 함수는 모든 조건이 True 인지를 확인하므로, 모든 위치에서의
        # 원소가 서로 같을 때 True가 됨
        
        
        if same:
            break
        # new_arr 와 change의 모든 원소가 서로 같으면 while문 종료
        
        # 변화가 있다면 계속 answer에 1을 추가하며 반복
        answer += 1
        
        new_arr = change
    
    return answer