s = input().upper()
S = list(set(s))
cnt = []
for i in S:
    cnt.append(s.count(i))

max_cnt = max(cnt) # 최댓값 저장
if cnt.count(max_cnt) >= 2:
    # cnt.count(max_cnt) => 최댓값의 개수
    print("?")
else:
    print(S[cnt.index(max_cnt)].upper())
    # S에서 최댓값의 인덱스를 찾고, 해당 인덱스에 해당하는 문자를 대문자로 출력