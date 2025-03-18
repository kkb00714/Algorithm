def solution(s):
    answer = []
    
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            if not answer: # ')' 이고 스택이 비어있는 경우
                return False
            answer.pop() # 스택이 비어있지 않은 경우
            
    return not answer