n = int(input())
tmp = 0
for _ in range(n):
    cnt = 0
    word = input()
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]: # 연속하는 두 문자가 다를 때
            word_list = word[i + 1 :] # 현재 문자열을 word_list에 할당
            if word_list.count(word[i]) > 0: # 새 문자열에서 현재 문자가 있다면
                cnt += 1
    if cnt == 0:
        tmp += 1
print(tmp)