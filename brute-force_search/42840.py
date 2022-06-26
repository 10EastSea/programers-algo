# 모의고사
def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    iters = [0, 0, 0, 0]
    matches = [0, 0, 0, 0]

    for a in answers:
        if first[iters[1]] == a: matches[1] += 1
        if second[iters[2]] == a: matches[2] += 1
        if third[iters[3]] == a: matches[3] += 1

        iters = list(map(lambda x: x+1, iters))
        if iters[1] == 5: iters[1] = 0
        if iters[2] == 8: iters[2] = 0
        if iters[3] == 10: iters[3] = 0
    
    best = max(matches)
    if matches[1] == best: answer.append(1)
    if matches[2] == best: answer.append(2)
    if matches[3] == best: answer.append(3)

    return answer