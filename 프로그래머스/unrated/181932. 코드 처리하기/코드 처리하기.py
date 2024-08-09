def solution(code):
    answer = ''
    idx = 0
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            else:
                if idx % 2 == 0: # idx 값이 짝수일 경우
                    answer += code[idx] # answer 값에 code[idx(짝수)]를 더함
                
        elif mode == 1:
            if code[idx] == '1':
                mode = 0
            else:
                if idx % 2 == 1: # idx 값이 홀수일 경우
                    answer += code[idx] # answer 값에 code[idx(홀수)]를 더함
        
    if answer == '':
        return 'EMPTY'
    else:
        return answer
    