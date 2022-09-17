# 모음 사전
answer, count = 0, 0
alpha = ['A', 'E', 'I', 'O', 'U']

def next_word(length, word, cmp_word):
    global answer, count
    
    if length == 0:
        for a in alpha:
            count += 1; next_word(length+1, str(a), cmp_word)
    elif length > 5: # 최대 문자 길이: 5
        count -= 1
    else:
        # print(count, word)
        if word == cmp_word: answer = count
        for a in alpha:
            count += 1; next_word(length+1, word+str(a), cmp_word)

def solution(word):           
    next_word(0, "", word)
    return answer