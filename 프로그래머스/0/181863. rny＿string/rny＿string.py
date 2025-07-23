def solution(rny_string):
    answer = ""
    if 'm' not in rny_string:
        return rny_string
    
    answer = rny_string.replace('m', 'rn')
    return answer