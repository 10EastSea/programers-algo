# K번째수
def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        tmp_array = array[i-1:j]
        tmp_array.sort()
        answer.append(tmp_array[k-1])

    return answer