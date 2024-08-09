def solution(myString):
    answer = []
    
    sentence = myString.split('x')
    sentence = [word for word in sentence if word != '']
    # 각 리스트의 요소를 순환하면서 만약 word가 빈 문자열이 아닌 경우에만 조건을 만족하도록 함
    
    sentence.sort()
    
    for i in range(len(sentence)):
        answer.append(sentence[i])
    
    return answer