import re

def solution(myStr):
    answer = []
    
    for x in re.split('[abc]', myStr):
        if not x:
            continue
        answer.append(x)
    
    if not answer:
        answer.append('EMPTY')
    
    return answer