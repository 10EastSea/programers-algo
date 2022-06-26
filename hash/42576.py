# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''

    participant_dict = {}
    for p in participant:
        value = participant_dict.get(p)
        if value is None: participant_dict[p] = 1
        else: participant_dict[p] += 1
    
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict[c] == 0: del participant_dict[c]

    for pd in participant_dict: answer = pd
    return answer