from collections import Counter

def solution(my_string):
    answer = []
    
    char_counts = Counter(my_string)
    # my_string의 각 문자의 등장 횟수를 카운트함
    
    for i in range(ord('A'), ord('Z') + 1):
        # A - Z 까지 char_counts에 x(알파벳)들이 y(얼마나)만큼 등장했는지 세어줌
        
        answer.append(char_counts[chr(i)])
        # A - Z 까지 순환을 마치고 char_counts에 해당 문자의 등장 횟수를 가져와서 answer에 append함
        
    for i in range(ord('a'), ord('z') + 1):
        # a - z 까지 char_counts에 x(알파벳)들이 y(얼마나)만큼 등장했는지 세어줌
        
        answer.append(char_counts[chr(i)])
        # a - z 까지 순환을 마치고 char_counts에 해당 문자의 등장 횟수를 가져와서 append 함
        
        # A - Z, a - z까지 두 번 끊은 이유
        # => ord('A'), ord('Z') 에서, 대문자와 소문자의 ASCII 코드가 다르기 때문
        
    return answer