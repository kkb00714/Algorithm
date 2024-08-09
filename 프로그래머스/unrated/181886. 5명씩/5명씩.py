def solution(names): # names = 걍 문자열임
    answer = []
    attraction = []
    
    
    for i in range(0, len(names), 5):
        attraction.append(names[i:i+5])
        
    for j in range(len(attraction)):
        answer.append(attraction[j][0]) 
        # 2차원 배열 형식
    
    
    return answer
